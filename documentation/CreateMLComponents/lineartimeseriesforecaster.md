# LinearTimeSeriesForecaster

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A time-series forecasting estimator.

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
struct LinearTimeSeriesForecaster<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Overview

> **Note**: Only `Float` and `Double` are currently supported as the Scalar type. You may get faster training when using `Float`.

## Topics

### Creating a linear time series forecaster
- [init(configuration: LinearTimeSeriesForecaster<Scalar>.Configuration)](./lineartimeseriesforecaster/init%28configuration%29.md)
  Creates a linear time-series forecaster.
### Inspecting a linear time series forecaster
- [let configuration: LinearTimeSeriesForecaster<Scalar>.Configuration](./lineartimeseriesforecaster/configuration-swift.property.md)
  The configuration.
- [var forecastWindowSize: Int](./lineartimeseriesforecaster/forecastwindowsize.md)
  The number of predicted samples.
- [var inputWindowSize: Int](./lineartimeseriesforecaster/inputwindowsize.md)
  The number of input samples.
### Updating and fitting
- [func update(inout LinearTimeSeriesForecaster<Scalar>.Transformer, with: AnnotatedBatch<Scalar>) async throws -> Scalar](./lineartimeseriesforecaster/update%28_,with%29.md)
  Updates a model with a new batch of examples.
- [func update(inout LinearTimeSeriesForecaster<Scalar>.Model, withWindows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](./lineartimeseriesforecaster/update%28_,withwindows,eventhandler%29.md)
  Updates a model with a sequence of windows.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](./lineartimeseriesforecaster/fitted%28to,eventhandler%29.md)
  Fits a model to a sequence of examples.
- [func fitted(to: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](./lineartimeseriesforecaster/fitted%28to,validateon,eventhandler%29.md)
  Fits a model to a sequence of examples with validation.
- [func fitted(toWindows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](./lineartimeseriesforecaster/fitted%28towindows,eventhandler%29.md)
  Fits a model to a sequence of windows.
- [func fitted(toWindows: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, validateOn: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws -> LinearTimeSeriesForecaster<Scalar>.Model](./lineartimeseriesforecaster/fitted%28towindows,validateon,eventhandler%29.md)
  Fits a model to a sequence of annotated windows with validation.
### Supporting types
- [LinearTimeSeriesForecaster.Configuration](./lineartimeseriesforecaster/configuration-swift.typealias.md)
- [LinearTimeSeriesForecaster.Model](./lineartimeseriesforecaster/model.md)
  A linear time-series forecasting model.
### Default Implementations
- [SupervisedEstimator Implementations](./lineartimeseriesforecaster/supervisedestimator-implementations.md)
- [UpdatableSupervisedEstimator Implementations](./lineartimeseriesforecaster/updatablesupervisedestimator-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SupervisedEstimator](./supervisedestimator.md)
- [UpdatableSupervisedEstimator](./updatablesupervisedestimator.md)

## See Also

### Time-based components
- [Creating a time-series classifier](./creating-a-time-series-classifier.md)
  Train a machine learning model to predict the class label of time-series signals.
- [Creating a time-series forecaster](./creating-a-time-series-forecaster.md)
  Forecast future data points by training a machine learning model using historical data.
- [struct DateFeatures](./datefeatures.md)
  A set of date and time features.
- [struct DateFeatureExtractor](./datefeatureextractor.md)
  A time and date feature extractor.
- [struct LinearTimeSeriesForecasterConfiguration](./lineartimeseriesforecasterconfiguration.md)
  The configuration for a linear time-series forecaster.
- [struct TimeSeriesForecasterBatches](./timeseriesforecasterbatches.md)
  A sequence of forecaster batches on a time series shaped array.
- [struct TimeSeriesForecasterAnnotatedWindows](./timeseriesforecasterannotatedwindows.md)
  A sequence of forecasting windows on a time series shaped array.
- [struct TemporalFeature](./temporalfeature.md)
  A temporal feature contains a segment identifier and a feature value.
- [protocol TemporalSequence](./temporalsequence.md)
  Async sequence for temporal features.
- [struct TemporalSegmentIdentifier](./temporalsegmentidentifier.md)
  Uniquely identifiers a segment of a temporal sequence.
- [struct SlidingWindows](./slidingwindows.md)
  A sequence of windows on a time series shaped array.
- [struct SlidingWindowTransformer](./slidingwindowtransformer.md)
  A temporal transformer that groups input elements.
- [struct Downsampler](./downsampler.md)
  A temporal transformer that down samples the input stream.
- [struct VideoReader](./videoreader.md)
  A video file reader.
- [struct TemporalFileSegment](./temporalfilesegment.md)
  A URL and a time range identifying a specific segment of a time-based (temporal) file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster)*