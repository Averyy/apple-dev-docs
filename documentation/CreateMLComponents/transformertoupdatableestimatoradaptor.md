# TransformerToUpdatableEstimatorAdaptor

**Framework**: Create ML Components  
**Kind**: struct

An updatable estimator that always returns a predefined transformer.

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
struct TransformerToUpdatableEstimatorAdaptor<Transformer> where Transformer : Transformer
```

## Topics

### Creating an estimator
- [init(Transformer)](transformertoupdatableestimatoradaptor/init(_:).md)
  Creates a trivial estimator.
### Getting the transformer
- [let transformer: Transformer](transformertoupdatableestimatoradaptor/transformer.md)
  A pre-defined transformer.
### Encoding and decoding
- [func encode(Transformer, to: inout any EstimatorEncoder) throws](transformertoupdatableestimatoradaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](transformertoupdatableestimatoradaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(Transformer, to: inout any EstimatorEncoder) throws](transformertoupdatableestimatoradaptor/encodewithoptimizer(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Transformer](transformertoupdatableestimatoradaptor/decodewithoptimizer(from:).md)
  Returns the pre-defined transformer.
### Fitting and updating
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Transformer](transformertoupdatableestimatoradaptor/fitted(to:eventhandler:).md)
  Returns the pre-defined transformer.
- [func makeTransformer() -> Transformer](transformertoupdatableestimatoradaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](transformertoupdatableestimatoradaptor/update(_:with:eventhandler:).md)
  Does nothing since this estimator uses a pre-defined transformer.
### Default Implementations
- [Estimator Implementations](transformertoupdatableestimatoradaptor/estimator-implementations.md)
- [UpdatableEstimator Implementations](transformertoupdatableestimatoradaptor/updatableestimator-implementations.md)

## Relationships

### Conforms To
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)
- [UpdatableEstimator](updatableestimator.md)

## See Also

- [struct TransformerToEstimatorAdaptor](transformertoestimatoradaptor.md)
  An estimator that always returns a predefined transformer.
- [struct TransformerToTemporalAdaptor](transformertotemporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor)*