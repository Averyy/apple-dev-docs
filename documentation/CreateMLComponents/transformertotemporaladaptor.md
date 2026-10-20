# TransformerToTemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A temporal transformer that applies a regular transformer to each value of a temporal sequence.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- iPadOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- Mac Catalyst 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- macOS 13.0+ - Deprecated in 15.0 (renamed: TemporalAdaptor)
- tvOS 16.0+ - Deprecated in 18.0 (renamed: TemporalAdaptor)
- visionOS 1.0+ - Deprecated in 2.0 (renamed: TemporalAdaptor)

## Declaration

```swift
struct TransformerToTemporalAdaptor<Base> where Base : Transformer
```

## Topics

### Creating a transformer
- [init(Base)](./transformertotemporaladaptor/init%28_%29.md)
  Creates a temporal transformer from a transformer.
### Applying
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> AnyTemporalSequence<TransformerToTemporalAdaptor<Base>.Output>](./transformertotemporaladaptor/applied%28to,eventhandler%29.md)
  Performs the transformation on each element of the input sequence.
- [TransformerToTemporalAdaptor.Input](./transformertotemporaladaptor/input.md)
  The input type.
- [TransformerToTemporalAdaptor.Output](./transformertotemporaladaptor/output.md)
  The output type.
- [TransformerToTemporalAdaptor.OutputSequence](./transformertotemporaladaptor/outputsequence.md)
  The output sequence type.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TemporalTransformer](./temporaltransformer.md)

## See Also

### Transformer adaptors
- [struct TransformerToEstimatorAdaptor](./transformertoestimatoradaptor.md)
  An estimator that always returns a predefined transformer.
- [struct TransformerToUpdatableEstimatorAdaptor](./transformertoupdatableestimatoradaptor.md)
  An updatable estimator that always returns a predefined transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertotemporaladaptor)*