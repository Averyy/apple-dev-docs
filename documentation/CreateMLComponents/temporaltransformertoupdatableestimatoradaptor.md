# TemporalTransformerToUpdatableEstimatorAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A temporal estimator that always returns a predefined temporal transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct TemporalTransformerToUpdatableEstimatorAdaptor<Transformer> where Transformer : TemporalTransformer
```

## Topics

### Creating an estimator
- [init(Transformer)](temporaltransformertoupdatableestimatoradaptor/init(_:).md)
  Creates a trivial estimator.
### Getting the transformer
- [let transformer: Transformer](temporaltransformertoupdatableestimatoradaptor/transformer.md)
  A pre-defined transformer.
### Encoding and decoding
- [func encode(Transformer, to: inout any EstimatorEncoder) throws](temporaltransformertoupdatableestimatoradaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](temporaltransformertoupdatableestimatoradaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(Transformer, to: inout any EstimatorEncoder) throws](temporaltransformertoupdatableestimatoradaptor/encodewithoptimizer(_:to:).md)
  This method is part of the conformance. It doesn’t encode anything since the transformer is pre-defined, so don’t call it.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Transformer](temporaltransformertoupdatableestimatoradaptor/decodewithoptimizer(from:).md)
  Returns the pre-defined transformer.
### Fitting and updating
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Transformer](temporaltransformertoupdatableestimatoradaptor/fitted(to:eventhandler:).md)
  Returns the pre-defined transformer.
- [func makeTransformer() -> Transformer](temporaltransformertoupdatableestimatoradaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](temporaltransformertoupdatableestimatoradaptor/update(_:with:eventhandler:).md)
  Does nothing since this estimator uses a pre-defined transformer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalEstimator](temporalestimator.md)
- [UpdatableTemporalEstimator](updatabletemporalestimator.md)

## See Also

- [struct TemporalAdaptor](temporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- [struct TemporalTransformerToEstimatorAdaptor](temporaltransformertoestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.
- [struct TemporalEstimatorToSupervisedAdaptor](temporalestimatortosupervisedadaptor.md)
  An adaptor that exposes a temporal estimator as a supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor)*