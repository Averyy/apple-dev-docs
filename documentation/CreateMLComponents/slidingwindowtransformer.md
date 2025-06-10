# SlidingWindowTransformer

**Framework**: Create ML Components  
**Kind**: struct

A temporal transformer that groups input elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct SlidingWindowTransformer<Input> where Input : Sendable
```

## Topics

### Creating a transformer
- [init(from: any Decoder) throws](slidingwindowtransformer/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(stride: Int, length: Int)](slidingwindowtransformer/init(stride:length:).md)
  Creates a window temporal transformer.
### Getting the properties
- [let length: Int](slidingwindowtransformer/length.md)
  The length of a window.
- [let stride: Int](slidingwindowtransformer/stride.md)
  The number of elements between the start of two consecutive windows.
### Performing the transformation
- [func applied<S>(to: S, eventHandler: EventHandler?) throws -> SlidingWindowTransformer<Input>.WindowSequence](slidingwindowtransformer/applied(to:eventhandler:).md)
  Extracts a window sequence from the input sequence
- [SlidingWindowTransformer.Input](slidingwindowtransformer/input.md)
  The input type.
- [SlidingWindowTransformer.Output](slidingwindowtransformer/output.md)
  The output type.
- [SlidingWindowTransformer.WindowSequence](slidingwindowtransformer/windowsequence.md)
  An async sequence of windows.
### Instance Methods
- [func encode(to: any Encoder) throws](slidingwindowtransformer/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [SlidingWindowTransformer.OutputSequence](slidingwindowtransformer/outputsequence.md)
  The output async sequence type.
### Default Implementations
- [TemporalTransformer Implementations](slidingwindowtransformer/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalTransformer](temporaltransformer.md)

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
- [struct Downsampler](downsampler.md)
  A temporal transformer that down samples the input stream.
- [struct VideoReader](videoreader.md)
  A video file reader.
- [struct TemporalFileSegment](temporalfilesegment.md)
  A URL and a time range identifying a specific segment of a time-based (temporal) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindowtransformer)*