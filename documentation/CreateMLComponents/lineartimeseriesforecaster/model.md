# LinearTimeSeriesForecaster.Model

**Framework**: Createmlcomponents  
**Kind**: struct

A linear time-series forecasting model.

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
struct Model
```

#### Overview

> **Note**: Only `Float` and `Double` are currently supported as the Scalar type.

## Topics

### Instance Properties
- [var annotationSize: Int](lineartimeseriesforecaster/model/annotationsize.md)
  The number of annotations per sample.
- [var bias: MLShapedArray<Scalar>?](lineartimeseriesforecaster/model/bias.md)
  The bias coefficients.
- [var featureSize: Int](lineartimeseriesforecaster/model/featuresize.md)
  The number of features per sample.
- [var forecastWindowSize: Int](lineartimeseriesforecaster/model/forecastwindowsize.md)
  The number of prediction samples.
- [var inputWindowSize: Int](lineartimeseriesforecaster/model/inputwindowsize.md)
  The number of input samples.
- [var stride: Int](lineartimeseriesforecaster/model/stride.md)
  The number of samples between windows.
- [var weight: MLShapedArray<Scalar>](lineartimeseriesforecaster/model/weight.md)
  The linear coefficients.
### Instance Methods
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](lineartimeseriesforecaster/model/applied(to:eventhandler:)-2wg7u.md)
  Performs a prediction on a shaped array of features.
- [func applied(to: some Sequence<MLShapedArray<Scalar>>, eventHandler: EventHandler?) async throws -> [MLShapedArray<Scalar>]](lineartimeseriesforecaster/model/applied(to:eventhandler:)-5kkin.md)
  Performs a prediction on a sequence of input features.
- [func applied(toWindow: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](lineartimeseriesforecaster/model/applied(towindow:eventhandler:).md)
  Performs a prediction on a window of input features.
- [func export(to: URL) throws](lineartimeseriesforecaster/model/export(to:).md)
  Exports this transformer as a CoreML model package.
- [func export(to: URL, metadata: ModelMetadata) throws](lineartimeseriesforecaster/model/export(to:metadata:).md)
  Exports this transformer as a CoreML model package with user-supplied metadata.
### Type Aliases
- [LinearTimeSeriesForecaster.Model.Input](lineartimeseriesforecaster/model/input.md)
  The input type.
- [LinearTimeSeriesForecaster.Model.Output](lineartimeseriesforecaster/model/output.md)
  The output type.
### Default Implementations
- [TemporalTransformer Implementations](lineartimeseriesforecaster/model/temporaltransformer-implementations.md)
- [Transformer Implementations](lineartimeseriesforecaster/model/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [TemporalTransformer](temporaltransformer.md)
- [Transformer](transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CreateMLComponents/lineartimeseriesforecaster/model)*