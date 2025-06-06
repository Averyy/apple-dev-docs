# Creating a time-series forecaster

**Framework**: Create ML Components

Forecast future data points by training a machine learning model using historical data.

#### Overview

Some signals have patterns that repeat over time or have clear trends. For example, the energy consumption of a city has a pattern with peaks in the evening when most people get home. It’s common practice to refer to these signals as time-series data. Other examples of time-series data are:

- The accelerometer on your phone when performing an action.
- The temperature of a machine in a factory.
- Your heart rate during a gym session.

Even though there are patterns to the data, these patterns aren’t trivial to forecast. You can perform forecasts on these data by training an ML model. For example, you can forecast future energy consumption based on historical consumption.

Training a time-series forecaster with the Create ML Components framework shares common training behavior with other model types.

##### Prepare Your Training Data

The first step to begin forecasting the energy consumption is to prepare the data. Gather the data as a CSV file, using the following structure:

| Date | Consumption |
| --- | --- |
| 2024-04-01 00:00:00 | 1.948 |
| 2024-04-01 01:00:00 | 1.678 |
| 2024-04-01 02:00:00 | 1.873 |
| 2024-04-01 03:00:00 | 1.604 |

The table shows a energy consumption reading for every hour (in GWh). Use the date and time because the consumption depends on the season and the time of day. Parse the date string into a `Date` type by using `CSVReadingOptions` and `Date.ParseStrategy`:

```swift
var options = CSVReadingOptions()
options.floatingPointType = .float
options.addDateParseStrategy(
    Date.ParseStrategy(
        format: "\(year: .defaultDigits)-\(month: .twoDigits)-\(day: .twoDigits) \(hour: .twoDigits(clock: .twentyFourHour, hourCycle: .zeroBased)):\(minute: .twoDigits):\(second: .twoDigits))",
        locale: Locale(identifier: "en_US"),
        timeZone: TimeZone(abbreviation: "GMT")!
    )
)
let dataFrame = try DataFrame(contentsOfCSVFile: url, columns: ["Date", "Temp"], types: ["Date": .date], options: options)
```

Now that you have a data frame with a `Date` column and a `Float` column, create a preprocessing pipeline. First, scale the training consumptions to have a normal distribution. This makes it easier for the model to learn. Take note of the mean and standard deviation to reverse this operation later.

```swift
// Compute the scale of the training portion.
let scalerEstimator = ColumnSelector<_, Float>(
    .include(columnNames: ["Temp"]),
    estimator: OptionalUnwrapper().appending(StandardScaler<Float>())
)
let trainingDataFrame = DataFrame(dataFrame[trainingPortion])
let scaler = try await scalerEstimator.fitted(to: trainingDataFrame)

// Scale the features.
let scaledDataFrame = try await scaler.applied(to: dataFrame)
let mean = scaler.transformers["Temp"]!.outer.mean
let stddev = scaler.transformers["Temp"]!.outer.standardDeviation
```

Extract features from the dates by using `DateFeatureExtractor`. The extractor creates values in the range `-0.5 ... 0.5` and represents the components you select. Concatenate all features into a single column of `MLShapedArray<Float>` values and create a features data frame.

```swift
// Extract the date features.
let dateFeatureExtractor = ColumnSelector<_, Date>(
    .include(columnNames: ["Date"]),
    transformer: OptionalUnwrapper().appending(
        DateFeatureExtractor<Float>(features: [.hour, .weekday, .day, .dayOfYear])
    )
)
// Concatenate the features.
let concatenator = ColumnConcatenator<Float>(
    columnSelection: .all,
    concatenatedColumnName: "Features"
)
let preprocessor = try await dateFeatureExtractor.appending(concatenator).fitted(to: scaledDataFrame)
let featuresDataFrame = try await preprocessor.applied(to: dataFrame)
```

Finally, extract features and annotations, and divide the data into training, validation, and testing sets:

```swift
let features = featuresDataFrame["Features", MLShapedArray<Float>.self]
    .filled(with: MLShapedArray<Float>())
let annotations = scaledDataFrame["Temp", Float.self]
    .filled(with: 0.0)
    .map({ MLShapedArray<Float>(scalars: [Float($0)], shape: [1]) })

// Create the training, validation, and testing splits.
let dayInHours = 24
let monthInHours = 30 * dayInHours
let yearInHours = 12 * monthInHours

let trainingPortion = 0 ..< yearInHours
let testingPotion = yearInHours + 4 * monthInHours - configuration.inputWindowSize ..< yearInHours + 8 * monthInHours
let validationPortion = yearInHours - configuration.inputWindowSize ..< yearInHours + 4 * monthInHours

let training = zip(features[trainingPortion], annotations[trainingPortion]).map(AnnotatedFeature.init)
let validation = zip(features[validationPortion], annotations[validationPortion]).map(AnnotatedFeature.init)
let testing = zip(features[testingPotion], annotations[testingPotion]).map(AnnotatedFeature.init)
```

##### Build and Train a Time Series Forecaster

After preparing your training data, you can create a forecaster. The forecaster configuration takes the input window size and forecast window size. Depending on your task you may want to adjust these values. A larger input window provides more context to the model, but results in a larger model. For this example, set the input window size to 14 days (336 samples) and the forecast window size to 4 days (96 samples).

```swift
var configuration = LinearTimeSeriesForecasterConfiguration(
    inputWindowSize: 14 * dayInHours,
    forecastWindowSize: 4 * dayInHours
)
configuration.maximumIterationCount = 20

let estimator = LinearTimeSeriesForecaster<Float>(configuration: configuration)
let model = try await estimator.fitted(to: training, validateOn: validation) { event in
    if let validationLoss = event.metrics[MetricsKey.validationLoss] as? Double {
        print("Validation loss: \(validationLoss)")
    }
}
```

##### Evaluate the Model

Use your testing set to evaluate your model. Two useful metrics you use to check a forecaster model are the mean-squared error (MSE) and the mean-absolute error (MAE).

```swift
var mseValues = [Double]()
var maeValues = [Double]()
let predictions = try await model.applied(to: testing.map(\.feature))
let groundTruths = testing.dropFirst(configuration.forecastWindowSize).map(\.annotation)
for (prediction, groundTruth) in zip(predictions, groundTruths) {
    let mse = meanSquaredError(prediction.scalars, groundTruth.scalars)
    let mae = meanAbsoluteError(prediction.scalars, groundTruth.scalars)
    mseValues.append(Double(mse))
    maeValues.append(Double(mae))
}

let mseSum = mseValues.reduce(0, +)
let mse = mseSum / Double(mseValues.count)
print("MSE: \(mse)")

let maeSum = maeValues.reduce(0, +)
let mae = maeSum / Double(maeValues.count)
print("MAE: \(mae)")
```

##### Export the Model

When you’re satisfied with the model’s accuracy, export it as a Core ML package:

```swift
try model.export(to: URL(filePath: "forecaster.mlpackage"))
```

Deploy the model you export and use Core ML to perform predictions. When you use the model, you need to concatenate the input window samples into a single shaped array. If you provide more than one window of input, the model returns multiple results in a shaped array.

```swift
let mlmodel = try MLModel(contentsOf: modelURL)
let testFeatures = MLShapedArray<Float>(
    concatenating: testing[0 ..< 14 * dayInHours].map(\.feature).map({ $0.expandingShape(at: 0) }),
    alongAxis: 0
)
let featureValue = MLFeatureValue(shapedArray: testFeatures)
let featureProvider = try MLDictionaryFeatureProvider(dictionary: ["input": featureValue])
let modelOutput = try await mlmodel.prediction(from: featureProvider)
let result = modelOutput.featureValue(for: "output")!.shapedArrayValue(of: Float.self)!
```

The model output provides scaled temperatures, so use the mean and standard deviation values to compute the temperatures:

```swift
let temperatures = result.scalars.map({ $0 * stddev + mean })
print(temperatures)
```

## See Also

- [Creating a time-series classifier](creating-a-time-series-classifier.md)
  Train a machine learning model to predict the class label of time-series signals.
- [struct DateFeatures](datefeatures.md)
  A set of date and time features.
- [struct DateFeatureExtractor](datefeatureextractor.md)
  A time and date feature extractor.
- [struct LinearTimeSeriesForecaster](lineartimeseriesforecaster.md)
  A time-series forecasting estimator.
- [struct LinearTimeSeriesForecasterConfiguration](lineartimeseriesforecasterconfiguration.md)
  The configuration for a linear time-series forecaster.
- [struct TimeSeriesForecasterBatches](timeseriesforecasterbatches.md)
  A sequence of forecaster batches on a time series shaped array.
- [struct TimeSeriesForecasterAnnotatedWindows](timeseriesforecasterannotatedwindows.md)
  A sequence of forecasting windows on a time series shaped array.
- [struct TemporalFeature](temporalfeature.md)
  A temporal feature contains a segment identifier and a feature value.
- [protocol TemporalSequence](temporalsequence.md)
  Async sequence for temporal features.
- [struct TemporalSegmentIdentifier](temporalsegmentidentifier.md)
  Uniquely identifiers a segment of a temporal sequence.
- [struct SlidingWindows](slidingwindows.md)
  A sequence of windows on a time series shaped array.
- [struct SlidingWindowTransformer](slidingwindowtransformer.md)
  A temporal transformer that groups input elements.
- [struct Downsampler](downsampler.md)
  A temporal transformer that down samples the input stream.
- [struct VideoReader](videoreader.md)
  A video file reader.
- [struct TemporalFileSegment](temporalfilesegment.md)
  A URL and a time range identifying a specific segment of a time-based (temporal) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/creating-a-time-series-forecaster)*