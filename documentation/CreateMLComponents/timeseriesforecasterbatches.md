# TimeSeriesForecasterBatches

**Framework**: Create ML Components  
**Kind**: struct

A sequence of forecaster batches on a time series shaped array.

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
struct TimeSeriesForecasterBatches<Scalar> where Scalar : MLShapedArrayScalar
```

#### Overview

A time-series forecaster takes a series of samples and produces a prediction of the next samples. For example the sequence `[1, 2, 3, 4]` could predict `[5, 6]`. To train a forecaster, each training batch contains the input samples along with the annotations (ground truth predictions). For example a batch could have this:

```None
features = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
]
annotations = [
    [5, 6],
    [6, 7],
    [7, 8],
]
```

The shape of the features in the sequence is `[batchSize, inputWindowSize, featureSize]` and the shape of the annotations is `[batchSize, forecastWindowSize, annotationSize]`. The batch sequence will return as many feature-annotation examples as fit in the input. For example, an input sequence size of 10 with an input sample count of 4 and a prediction sample count of 2 will produce 5 examples:

```None
features: [1, 2, 3, 4], annotations: [5, 6]
features: [2, 3, 4, 5], annotations: [6, 7]
features: [3, 4, 5, 6], annotations: [7, 8]
features: [4, 5, 6, 7], annotations: [8, 9]
features: [5, 6, 7, 8], annotations: [9, 10]
```

Note that 9 and 10 are never used as features because there would be no annotations for those examples.

## Topics

### Initializers
- [init(features: MLShapedArray<Scalar>, annotations: MLShapedArray<Scalar>, batchSize: Int, inputWindowSize: Int, forecastWindowSize: Int, shufflesBatches: Bool) throws](timeseriesforecasterbatches/init(features:annotations:batchsize:inputwindowsize:forecastwindowsize:shufflesbatches:).md)
  Creates a batch sequence.
### Instance Properties
- [let annotations: MLShapedArray<Scalar>](timeseriesforecasterbatches/annotations.md)
  The original annotations.
- [let batchSize: Int](timeseriesforecasterbatches/batchsize.md)
  The batch size.
- [let features: MLShapedArray<Scalar>](timeseriesforecasterbatches/features.md)
  The original features.
- [let forecastWindowSize: Int](timeseriesforecasterbatches/forecastwindowsize.md)
  The prediction sample count.
- [let inputWindowSize: Int](timeseriesforecasterbatches/inputwindowsize.md)
  The input sample count.
- [var shufflesBatches: Bool](timeseriesforecasterbatches/shufflesbatches.md)
  A Boolean value indicating whether to shuffle the batches.
- [var underestimatedCount: Int](timeseriesforecasterbatches/underestimatedcount.md)
  A value less than or equal to the number of elements in the sequence, calculated nondestructively.
### Instance Methods
- [func makeIterator() -> TimeSeriesForecasterBatches<Scalar>.Iterator](timeseriesforecasterbatches/makeiterator.md)
  Returns an iterator over the elements of this sequence.
### Type Aliases
- [TimeSeriesForecasterBatches.Element](timeseriesforecasterbatches/element.md)
  A type representing the sequence’s elements.
### Default Implementations
- [Sequence Implementations](timeseriesforecasterbatches/sequence-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterbatches)*