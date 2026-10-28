# LinearTimeSeriesForecaster.Model

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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

Available when `Scalar` conforms to `MLShapedArrayScalar` and `BinaryFloatingPoint`.

## Overview

> **Note**: Only `Float` and `Double` are currently supported as the Scalar type.

## Topics

### Inspecting the model
- [var annotationSize: Int](./model/annotationsize.md)
  The number of annotations per sample.
- [var bias: MLShapedArray<Scalar>?](./model/bias.md)
  The bias coefficients.
- [var featureSize: Int](./model/featuresize.md)
  The number of features per sample.
- [var forecastWindowSize: Int](./model/forecastwindowsize.md)
  The number of prediction samples.
- [var inputWindowSize: Int](./model/inputwindowsize.md)
  The number of input samples.
- [var stride: Int](./model/stride.md)
  The number of samples between windows.
- [var weight: MLShapedArray<Scalar>](./model/weight.md)
  The linear coefficients.
### Applying the model
- [func applied(to:eventHandler:)](./model/applied%28to,eventhandler%29.md)
  Performs a prediction on a shaped array of features.
- [func applied(toWindow: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](./model/applied%28towindow,eventhandler%29.md)
  Performs a prediction on a window of input features.
### Exporting the model
- [func export(to: URL) throws](./model/export%28to%29.md)
  Exports this transformer as a CoreML model package.
- [func export(to: URL, metadata: ModelMetadata) throws](./model/export%28to,metadata%29.md)
  Exports this transformer as a CoreML model package with user-supplied metadata.
### Default Implementations
- [TemporalTransformer Implementations](./model/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [TemporalTransformer](../temporaltransformer.md)
- [Transformer](../transformer.md)

## See Also

### Supporting types
- [LinearTimeSeriesForecaster.Configuration](./configuration-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/model)*