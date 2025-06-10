# TemporalEstimatorToSupervisedAdaptor

**Framework**: Create ML Components  
**Kind**: struct

An adaptor that exposes a temporal estimator as a supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation> where Estimator : TemporalEstimator, Annotation : Equatable, Annotation : Sendable
```

## Topics

### Creating an adaptor
- [init(Estimator)](temporalestimatortosupervisedadaptor/init(_:).md)
  Creates a temporal estimator adaptor.
### Getting the estimator
- [let estimator: Estimator](temporalestimatortosupervisedadaptor/estimator.md)
  The wrapped estimator.
### Encoding and decoding
- [func encode(TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](temporalestimatortosupervisedadaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](temporalestimatortosupervisedadaptor/decode(from:).md)
  Returns the pre-defined transformer.
### Fitting
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](temporalestimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> TemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](temporalestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [TemporalEstimatorToSupervisedAdaptor.Transformer](temporalestimatortosupervisedadaptor/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedTemporalEstimator Implementations](temporalestimatortosupervisedadaptor/supervisedtemporalestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedTemporalEstimator](supervisedtemporalestimator.md)

## See Also

- [struct TemporalAdaptor](temporaladaptor.md)
  A temporal transformer that applies a regular transformer to each value of a temporal sequence.
- [struct TemporalTransformerToEstimatorAdaptor](temporaltransformertoestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.
- [struct TemporalTransformerToUpdatableEstimatorAdaptor](temporaltransformertoupdatableestimatoradaptor.md)
  A temporal estimator that always returns a predefined temporal transformer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimatortosupervisedadaptor)*