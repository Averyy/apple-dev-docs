# TransformerToTemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A temporal transformer that applies a regular transformer to each value of a temporal sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct TransformerToTemporalAdaptor<Base> where Base : Transformer
```

## Topics

### Creating a transformer
- [init(Base)](transformertotemporaladaptor/init(_:).md)
  Creates a temporal transformer from a transformer.
### Applying
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output>](transformertotemporaladaptor/applied(to:eventhandler:).md)
  Performs the transformation on each element of the input sequence.
- [TransformerToTemporalAdaptor.Input](transformertotemporaladaptor/input.md)
  The input type.
- [TransformerToTemporalAdaptor.Output](transformertotemporaladaptor/output.md)
  The output type.
- [TransformerToTemporalAdaptor.OutputSequence](transformertotemporaladaptor/outputsequence.md)
  The output sequence type.
### Default Implementations
- [TemporalTransformer Implementations](transformertotemporaladaptor/temporaltransformer-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalTransformer](temporaltransformer.md)

## See Also

- [struct TransformerToEstimatorAdaptor](transformertoestimatoradaptor.md)
  An estimator that always returns a predefined transformer.
- [struct TransformerToUpdatableEstimatorAdaptor](transformertoupdatableestimatoradaptor.md)
  An updatable estimator that always returns a predefined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor)*