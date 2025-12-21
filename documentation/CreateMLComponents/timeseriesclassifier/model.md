# TimeSeriesClassifier.Model

**Framework**: Create ML Components  
**Kind**: struct

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

#### Overview

> **Note**: Only `Float` and `Double` are currently supported as the Scalar type.

## Topics

### Getting the stride
- [var stride: Int](timeseriesclassifier/model/stride.md)
  The number of samples between temporal predictions.
### Applying and exporting
- [func applied(to:eventHandler:)](timeseriesclassifier/model/applied(to:eventhandler:).md)
  Performs a classification on a shaped array of input features.
- [func export(to: URL) throws](timeseriesclassifier/model/export(to:).md)
  Exports this transformer as a CoreML model package.
- [func export(to: URL, metadata: ModelMetadata) throws](timeseriesclassifier/model/export(to:metadata:).md)
  Exports this transformer as a CoreML model package with user-supplied metadata.
### Default Implementations
- [TemporalTransformer Implementations](timeseriesclassifier/model/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalTransformer](temporaltransformer.md)
- [Transformer](transformer.md)

## See Also

- [TimeSeriesClassifier.Configuration](timeseriesclassifier/configuration-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/model)*