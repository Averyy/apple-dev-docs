# TransformerToEstimatorAdaptor

**Framework**: Create ML Components  
**Kind**: struct

An estimator that always returns a predefined transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct TransformerToEstimatorAdaptor<Transformer> where Transformer : Transformer
```

## Topics

### Creating a feature
- [init(Transformer)](transformertoestimatoradaptor/init(_:).md)
  Creates a trivial estimator.
### Getting the transformer
- [let transformer: Transformer](transformertoestimatoradaptor/transformer.md)
  A pre-defined transformer.
### Encoding and Decoding
- [func encode(Transformer, to: inout any EstimatorEncoder) throws](transformertoestimatoradaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](transformertoestimatoradaptor/decode(from:).md)
  Returns the pre-defined transformer.
### Fitting
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Transformer](transformertoestimatoradaptor/fitted(to:eventhandler:).md)
  Returns the pre-defined transformer.

## Relationships

### Conforms To
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct TransformerToTemporalAdaptor](transformertotemporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- [struct TransformerToUpdatableEstimatorAdaptor](transformertoupdatableestimatoradaptor.md)
  An updatable estimator that always returns a predefined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoestimatoradaptor)*