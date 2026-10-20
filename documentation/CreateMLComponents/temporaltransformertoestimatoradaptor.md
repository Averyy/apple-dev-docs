# TemporalTransformerToEstimatorAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A temporal estimator that always returns a predefined temporal transformer.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
struct TemporalTransformerToEstimatorAdaptor<Transformer> where Transformer : TemporalTransformer
```

## Topics

### Creating an estimator
- [init(Transformer)](./temporaltransformertoestimatoradaptor/init%28_%29.md)
  Creates a trivial estimator.
### Getting the transformer
- [let transformer: Transformer](./temporaltransformertoestimatoradaptor/transformer.md)
  A pre-defined transformer.
### Encoding and decoding
- [func encode(Transformer, to: inout any EstimatorEncoder) throws](./temporaltransformertoestimatoradaptor/encode%28_,to%29.md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](./temporaltransformertoestimatoradaptor/decode%28from%29.md)
  Returns the pre-defined transformer.
### Fitting
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Transformer](./temporaltransformertoestimatoradaptor/fitted%28to,eventhandler%29.md)
  Returns the pre-defined transformer.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TemporalEstimator](./temporalestimator.md)

## See Also

### Temporal adaptors
- [struct TemporalAdaptor](./temporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- [struct TemporalEstimatorToSupervisedAdaptor](./temporalestimatortosupervisedadaptor.md)
  An adaptor that exposes a temporal estimator as a supervised temporal estimator.
- [struct TemporalTransformerToUpdatableEstimatorAdaptor](./temporaltransformertoupdatableestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoestimatoradaptor)*