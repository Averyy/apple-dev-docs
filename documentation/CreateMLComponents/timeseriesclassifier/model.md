# TimeSeriesClassifier.Model

**Framework**: Createmlcomponents  
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

### Instance Properties
- [var stride: Int](timeseriesclassifier/model/stride.md)
  The number of samples between temporal predictions.
### Instance Methods
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> ClassificationDistribution<Label>](timeseriesclassifier/model/applied(to:eventhandler:)-x9iv.md)
  Performs a classification on a shaped array of input features.
- [func export(to: URL) throws](timeseriesclassifier/model/export(to:).md)
  Exports this transformer as a CoreML model package.
- [func export(to: URL, metadata: ModelMetadata) throws](timeseriesclassifier/model/export(to:metadata:).md)
  Exports this transformer as a CoreML model package with user-supplied metadata.
### Type Aliases
- [TimeSeriesClassifier.Model.Input](timeseriesclassifier/model/input.md)
  The input type.
- [TimeSeriesClassifier.Model.Output](timeseriesclassifier/model/output.md)
  The output type.
### Default Implementations
- [Decodable Implementations](timeseriesclassifier/model/decodable-implementations.md)
- [Encodable Implementations](timeseriesclassifier/model/encodable-implementations.md)
- [TemporalTransformer Implementations](timeseriesclassifier/model/temporaltransformer-implementations.md)
- [Transformer Implementations](timeseriesclassifier/model/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [TemporalTransformer](temporaltransformer.md)
- [Transformer](transformer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CreateMLComponents/timeseriesclassifier/model)*