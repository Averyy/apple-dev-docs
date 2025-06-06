# Creating a time-series classifier

**Framework**: Create ML Components

Train a machine learning model to predict the class label of time-series signals.

#### Overview

Some signals have patterns that repeat over time or have clear trends. For example, the accelerometer data from an Apple Watch while the wearer is exercising. It’s common practice to refer to these signals as . Other examples of time-series data are:

- The temperature of a machine in a factory.
- Your heart rate during a gym session.
- The audio signal in a song.

Even though there are patterns to the data, these patterns aren’t trivial to classify. You can perform classification on these data by training an ML model. For example, you can classify hand gestures from the accelerometer data from an Apple Watch.

Training a time-series classifier with the Create ML Components framework shares common training behavior with other model types.

##### Prepare Your Training Data

The first step to begin classifying the throwing movement of a baseball is to prepare the data. The model predicts the baseball throw as fastball, breaking ball, or changeup. Organize the data by using the following directory structure:

```None
/
    fastball/
        recording1.csv
        recording2.csv
        ...
    breaking/
        recording3.csv
        recording4.csv
        ...
    changeup/
        recording5.csv
        recording6.csv
        ...
```

Each move contains a subdirectory with CSV files that contains information about a throw.
Each data file represents one throw and uses the following structure:

| accelerometerAccelerationX(G) | accelerometerAccelerationY(G) | accelerometerAccelerationZ(G) | motionRotationRateX(rad/s) | motionRotationRateY(rad/s) | motionRotationRateZ(rad/s) |
| --- | --- | --- | --- | --- | --- |
| 0.031036 | 0.056931 | -1.005661 | 0.05611 | -0.029355 | -0.023368 |
| 0.02655 | 0.04863 | -0.996994 | 0.096923 | -0.040154 | -0.020962 |
| 0.023743 | 0.045242 | -1.004333 | 0.053917 | -0.033634 | -0.016979 |

The table shows the acceleration and rotation rate for a thrown baseball. You use these data points to identify the trajectory of the object that helps the model learn the throwing pattern. Each column denotes a feature for the model. Read the training data files from the directory by using `AnnotatedFiles`:

```swift
let annotatedFiles = try AnnotatedFiles(
    labeledBySubdirectoryNamesAt: url,
    type: .commaSeparatedText,
    continueOnFailure: true
)
```

The recordings you produce may have differing time durations, resulting in a different number of rows for each CSV file you associate with it. Configure the maximum number of samples that the framework classifies by using `maximumSequenceLength`:

```swift
var configuration = TimeSeriesClassifierConfiguration()
configuration.maximumSequenceLength = 120
```

The next step is to process each CSV file into an `AnnotatedFeature` and process the features as an `MLShapedArray` with a label as a String.

```swift
let featureColumns = [
    "accelerometerAccelerationX(G)",
    "accelerometerAccelerationY(G)",
    "accelerometerAccelerationZ(G)",
    "motionRotationRateX(rad/s)",
    "motionRotationRateY(rad/s)",
    "motionRotationRateZ(rad/s)"
]

let options = CSVReadingOptions(floatingPointType: .float)
var result = [AnnotatedFeature<MLShapedArray<Float>, String>]()
for file in annotatedFiles {
    let df = try DataFrame(contentsOfCSVFile: file.feature, columns: featureColumns, options: options)
    var arrays = [MLShapedArray<Float>]()
    for featureColumn in featureColumns {
        let featureValues = df[featureColumn, Float.self].filled(with: .nan)
        let processedFeatureValues: MLShapedArray<Float>
        if featureValues.count > configuration.maximumSequenceLength {
            processedFeatureValues = MLShapedArray(
                scalars: featureValues[..<configuration.maximumSequenceLength],
                shape: [configuration.maximumSequenceLength, 1]
            )
        } else {
            processedFeatureValues = MLShapedArray(scalars: featureValues, shape: [featureValues.count, 1])
        }
        arrays.append(processedFeatureValues)
    }

    let feature = MLShapedArray(concatenating: arrays, alongAxis: 1)
    result.append(AnnotatedFeature(feature: feature, annotation: file.annotation))
}

// Shuffle the samples to introduce randomness.
result.shuffle()
```

Finally, divide the data into training, validation, and testing sets where 80 percent of the data goes into the training set, and 10 percent each for validation and testing.

```swift
let sampleCount = Double(result.count)
let training = result[0 ..< Int(sampleCount * 0.8)]
let validation = result[Int(sampleCount * 0.8) ..< Int(sampleCount * 0.9)]
let testing = result[Int(sampleCount * 0.9)...]
```

##### Build and Train a Time Series Classifier

After preparing your training data, configure your classifier model with the number of training iterations and class labels:

```swift
configuration.maximumIterationCount = 5

let estimator = TimeSeriesClassifier<Float, String>(
    labels: ["fastball", "breaking", "changeup", "other"],
    configuration: configuration
)
```

Train your classifier model and print the training and validation accuracy at every iteration to monitor the progress:

```None
swift
let model = try await estimator.fitted(to: training, validateOn: validation) { event in
    if let trainingAccuracy = event.metrics[MetricsKey.trainingAccuracy] as? Double {
        print("Training accuracy: \(trainingAccuracy)")
    }
    if let validationAccuracy = event.metrics[MetricsKey.validationAccuracy] as? Double {
        print("Validation accuracy: \(validationAccuracy)")
    }
}
```

##### Evaluate the Model

Use your testing set to evaluate your model. Classification provides an accuracy metric with a value between 0 and 1, where 0 represents the least accurate. Look at how accurate it classified your labeled test data to determine whether to export the model.

```swift
let classificationDistributions = try await model.applied(to: testing.map(\.feature))
let predictedLabels = classificationDistributions.map(\.mostLikelyLabel!)
let metrics = ClassificationMetrics(predictedLabels, testing.map(\.annotation))

print("Accuracy: (metrics.accuracy)")
```

##### Export the Model

When you’re satisfied with the model’s accuracy, export it as a Core ML package:

```swift
try model.export(to: URL(filePath: "classifier.mlpackage"))
```

Deploy the model you export and use Core ML to perform predictions. When you use the model, create a single shaped array of features with the shape `[sequenceLength, 1]`:.

```swift
let mlmodel = try MLModel(contentsOf: modelURL)
let featureValue = MLFeatureValue(shapedArray: features)
let featureProvider = try MLDictionaryFeatureProvider(
    dictionary: [
        "input": featureValue,
        "sequenceLength": MLFeatureValue(shapedArray: MLShapedArray(scalars: [Int32(sequenceLength)], shape: [1])),
    ]
)
let modelOutput = try await model.prediction(from: featureProvider)
let probabilities = modelOutput.featureValue(for: "labelProbabilities")!.dictionaryValue as! [String: NSNumber]
let label = probabilities.max(by: { $0.value.doubleValue < $1.value.doubleValue })?.key
```

## See Also

- [Creating a time-series forecaster](creating-a-time-series-forecaster.md)
  Forecast future data points by training a machine learning model using historical data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/creating-a-time-series-classifier)*