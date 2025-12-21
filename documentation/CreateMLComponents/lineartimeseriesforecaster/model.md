# LinearTimeSeriesForecaster.Model

**Framework**: Create ML Components  
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

### Inspecting the model
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
### Applying the model
- [func applied(to:eventHandler:)](lineartimeseriesforecaster/model/applied(to:eventhandler:).md)
  Performs a prediction on a shaped array of features.
- [func applied(toWindow: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](lineartimeseriesforecaster/model/applied(towindow:eventhandler:).md)
  Performs a prediction on a window of input features.
### Exporting the model
- [func export(to: URL) throws](lineartimeseriesforecaster/model/export(to:).md)
  Exports this transformer as a CoreML model package.
- [func export(to: URL, metadata: ModelMetadata) throws](lineartimeseriesforecaster/model/export(to:metadata:).md)
  Exports this transformer as a CoreML model package with user-supplied metadata.
### Default Implementations
- [TemporalTransformer Implementations](lineartimeseriesforecaster/model/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalTransformer](temporaltransformer.md)
- [Transformer](transformer.md)

## See Also

- [LinearTimeSeriesForecaster.Configuration](lineartimeseriesforecaster/configuration-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model)*