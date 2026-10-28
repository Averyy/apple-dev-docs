# TimeSeriesClassifier.Model

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A time-series classifier model.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Model
```

Available when `Scalar` conforms to `MLShapedArrayScalar`, `Scalar` conforms to `BinaryFloatingPoint`, `Label` conforms to `Comparable`, `Label` conforms to `Decodable`, `Label` conforms to `Encodable`, and `Label` conforms to `Hashable`.

## Overview

> **Note**: Only `Float` and `Double` are currently supported as the Scalar type.

## Topics

### Getting the stride
- [var stride: Int](./model/stride.md)
  The number of samples between temporal predictions.
### Applying and exporting
- [func applied(to:eventHandler:)](./model/applied%28to,eventhandler%29.md)
  Performs a classification on a shaped array of input features.
- [func export(to: URL) throws](./model/export%28to%29.md)
  Exports this transformer as a CoreML model package.
- [func export(to: URL, metadata: ModelMetadata) throws](./model/export%28to,metadata%29.md)
  Exports this transformer as a CoreML model package with user-supplied metadata.
### Default Implementations
- [TemporalTransformer Implementations](./model/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [TemporalTransformer](../temporaltransformer.md)
- [Transformer](../transformer.md)

## See Also

### Supporting types
- [TimeSeriesClassifier.Configuration](./configuration-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model)*