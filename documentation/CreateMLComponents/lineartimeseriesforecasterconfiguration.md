# LinearTimeSeriesForecasterConfiguration

**Framework**: Create ML Components  
**Kind**: struct

The configuration for a linear time-series forecaster.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct LinearTimeSeriesForecasterConfiguration
```

## Topics

### Operators
- [static func == (LinearTimeSeriesForecasterConfiguration, LinearTimeSeriesForecasterConfiguration) -> Bool](lineartimeseriesforecasterconfiguration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](lineartimeseriesforecasterconfiguration/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(inputWindowSize: Int, forecastWindowSize: Int)](lineartimeseriesforecasterconfiguration/init(inputwindowsize:forecastwindowsize:).md)
  Creates a configuration.
### Instance Properties
- [var batchSize: Int](lineartimeseriesforecasterconfiguration/batchsize.md)
  The number of examples in each training batch.
- [var earlyStoppingIterationCount: Int](lineartimeseriesforecasterconfiguration/earlystoppingiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var earlyStoppingTolerance: Float](lineartimeseriesforecasterconfiguration/earlystoppingtolerance.md)
  The early-stopping tolerance.
- [var forecastWindowSize: Int](lineartimeseriesforecasterconfiguration/forecastwindowsize.md)
  The number of predicted samples.
- [var hashValue: Int](lineartimeseriesforecasterconfiguration/hashvalue.md)
  The hash value.
- [var inputWindowSize: Int](lineartimeseriesforecasterconfiguration/inputwindowsize.md)
  The number of input samples.
- [var learningRate: Float](lineartimeseriesforecasterconfiguration/learningrate.md)
  The starting learning rate.
- [var maximumIterationCount: Int](lineartimeseriesforecasterconfiguration/maximumiterationcount.md)
  The maximum number of allowed passes through the data.
- [var randomSeed: Int?](lineartimeseriesforecasterconfiguration/randomseed.md)
  A seed to generate reproducible results from random operations.
### Instance Methods
- [func encode(to: any Encoder) throws](lineartimeseriesforecasterconfiguration/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](lineartimeseriesforecasterconfiguration/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](lineartimeseriesforecasterconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating a time-series classifier](creating-a-time-series-classifier.md)
  Train a machine learning model to predict the class label of time-series signals.
- [Creating a time-series forecaster](creating-a-time-series-forecaster.md)
  Forecast future data points by training a machine learning model using historical data.
- [struct DateFeatures](datefeatures.md)
  A set of date and time features.
- [struct DateFeatureExtractor](datefeatureextractor.md)
  A time and date feature extractor.
- [struct LinearTimeSeriesForecaster](lineartimeseriesforecaster.md)
  A time-series forecasting estimator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecasterconfiguration)*