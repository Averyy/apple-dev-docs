# TemporalEstimatorToSupervisedAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An adaptor that exposes a temporal estimator as a supervised temporal estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
struct TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation> where Estimator : TemporalEstimator, Annotation : Equatable, Annotation : Sendable
```

## Topics

### Creating an adaptor
- [init(Estimator)](./temporalestimatortosupervisedadaptor/init%28_%29.md)
  Creates a temporal estimator adaptor.
### Getting the estimator
- [let estimator: Estimator](./temporalestimatortosupervisedadaptor/estimator.md)
  The wrapped estimator.
### Encoding and decoding
- [func encode(TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](./temporalestimatortosupervisedadaptor/encode%28_,to%29.md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](./temporalestimatortosupervisedadaptor/decode%28from%29.md)
  Returns the pre-defined transformer.
### Fitting
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](./temporalestimatortosupervisedadaptor/fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](./temporalestimatortosupervisedadaptor/fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [protocol Transformer](./transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SupervisedTemporalEstimator](./supervisedtemporalestimator.md)

## See Also

### Temporal adaptors
- [struct TemporalAdaptor](./temporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- [struct TemporalTransformerToEstimatorAdaptor](./temporaltransformertoestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.
- [struct TemporalTransformerToUpdatableEstimatorAdaptor](./temporaltransformertoupdatableestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimatortosupervisedadaptor)*