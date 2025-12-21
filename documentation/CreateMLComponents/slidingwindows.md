# SlidingWindows

**Framework**: Create ML Components  
**Kind**: struct

A sequence of windows on a time series shaped array.

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
struct SlidingWindows<Scalar> where Scalar : MLShapedArrayScalar
```

#### Overview

The shape of each window in the sequence is `[length, featureSize]`. The sequence will return as many windows as fit in the input. For example, an input shaped array of shape `[8, 1]` using `stride` of 1 and `length` of 4 will produce 5 examples:

```None
[[1], [2], [3], [4]]
[[2], [3], [4], [5]]
[[3], [4], [5], [6]]
[[4], [5], [6], [7]]
[[5], [6], [7], [8]]
```

## Topics

### Creating a sliding window
- [init(input: MLShapedArray<Scalar>, length: Int, stride: Int) throws](slidingwindows/init(input:length:stride:).md)
  Creates a sliding windows sequence.
### Inspecting the sliding window
- [var endIndex: Int](slidingwindows/endindex.md)
  The collection’s “past the end” position–that is, the position one greater than the last valid subscript argument.
- [let input: MLShapedArray<Scalar>](slidingwindows/input.md)
  The input shaped array.
- [let length: Int](slidingwindows/length.md)
  The number samples in each window.
- [var startIndex: Int](slidingwindows/startindex.md)
  The position of the first window.
- [let stride: Int](slidingwindows/stride.md)
  The number of samples between windows.
### Getting the index
- [func index(Int, offsetBy: Int) -> Int](slidingwindows/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(after: Int) -> Int](slidingwindows/index(after:).md)
  Returns the position immediately after the given index.
- [func index(before: Int) -> Int](slidingwindows/index(before:).md)
  Returns the position immediately before the given index.
### Getting the subscript
- [subscript(_:)](slidingwindows/subscript(_:).md)
  Accesses a contiguous range of windows.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

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
- [struct SlidingWindowTransformer](slidingwindowtransformer.md)
  A temporal transformer that groups input elements.
- [struct Downsampler](downsampler.md)
  A temporal transformer that down samples the input stream.
- [struct VideoReader](videoreader.md)
  A video file reader.
- [struct TemporalFileSegment](temporalfilesegment.md)
  A URL and a time range identifying a specific segment of a time-based (temporal) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/slidingwindows)*