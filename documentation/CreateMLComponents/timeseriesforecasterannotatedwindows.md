# TimeSeriesForecasterAnnotatedWindows

**Framework**: Create ML Components  
**Kind**: struct

A sequence of forecasting windows on a time series shaped array.

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
struct TimeSeriesForecasterAnnotatedWindows<Scalar> where Scalar : MLShapedArrayScalar
```

#### Overview

A time-series forecaster takes a series of samples and produces a prediction of the next samples. For example the sequence `[1, 2, 3, 4]` could predict `[5, 6]`.

The shape of each feature in the sequence is `[inputWindowSize, featureSize]` and the shape of each annotation is `[forecastWindowSize, annotationSize]`. The sequence will return as many feature-annotation examples as fit in the input. For example an input sequence of size of 10 with an input sample count of 4, a prediction sample count of 2, and a stride of 1 will produce 5 annotated windows:

```None
feature: [1, 2, 3, 4], annotation: [5, 6]
feature: [2, 3, 4, 5], annotation: [6, 7]
feature: [3, 4, 5, 6], annotation: [7, 8]
feature: [4, 5, 6, 7], annotation: [8, 9]
feature: [5, 6, 7, 8], annotation: [9, 10]
```

Note that 9 and 10 are never used as features because there would be no annotations for those samples.

## Topics

### Initializers
- [init(features: MLShapedArray<Scalar>, annotations: MLShapedArray<Scalar>, inputWindowSize: Int, forecastWindowSize: Int, stride: Int, shufflesElements: Bool) throws](timeseriesforecasterannotatedwindows/init(features:annotations:inputwindowsize:forecastwindowsize:stride:shuffleselements:).md)
  Creates a batch sequence.
### Instance Properties
- [let annotations: MLShapedArray<Scalar>](timeseriesforecasterannotatedwindows/annotations.md)
  The original annotations.
- [let features: MLShapedArray<Scalar>](timeseriesforecasterannotatedwindows/features.md)
  The original features.
- [let forecastWindowSize: Int](timeseriesforecasterannotatedwindows/forecastwindowsize.md)
  The prediction sample count.
- [let inputWindowSize: Int](timeseriesforecasterannotatedwindows/inputwindowsize.md)
  The input sample count.
- [var shufflesElements: Bool](timeseriesforecasterannotatedwindows/shuffleselements.md)
  A Boolean value indicating whether to shuffle the elements.
- [var stride: Int](timeseriesforecasterannotatedwindows/stride.md)
  The number of samples between windows.
- [var underestimatedCount: Int](timeseriesforecasterannotatedwindows/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func makeIterator() -> TimeSeriesForecasterAnnotatedWindows<Scalar>.Iterator](timeseriesforecasterannotatedwindows/makeiterator.md)
  Returns an iterator over the elements of this sequence.
### Type Aliases
- [TimeSeriesForecasterAnnotatedWindows.Element](timeseriesforecasterannotatedwindows/element.md)
  A type representing the sequence’s elements.
### Default Implementations
- [Sequence Implementations](timeseriesforecasterannotatedwindows/sequence-implementations.md)

## Relationships

### Conforms To
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterannotatedwindows)*