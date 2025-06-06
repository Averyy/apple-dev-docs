# UpdatableTemporalEstimatorToSupervisedAdaptor

**Framework**: Create ML Components  
**Kind**: struct

An adaptor that exposes an updatable temporal estimator as an updatable supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation> where Estimator : UpdatableTemporalEstimator, Annotation : Equatable, Annotation : Sendable
```

## Topics

### Creating an adaptor
- [init(Estimator)](updatabletemporalestimatortosupervisedadaptor/init(_:).md)
  Creates a temporal estimator adaptor.
### Getting the estimator
- [let estimator: Estimator](updatabletemporalestimatortosupervisedadaptor/estimator.md)
  The wrapped estimator.
### Encoding and decoding
- [func encode(UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](updatabletemporalestimatortosupervisedadaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](updatabletemporalestimatortosupervisedadaptor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
### Fitting and updating
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatabletemporalestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func makeTransformer() -> Estimator.Transformer](updatabletemporalestimatortosupervisedadaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatabletemporalestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, Validation, FeatureSequence>(inout UpdatableTemporalEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, with: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws](updatabletemporalestimatortosupervisedadaptor/update(_:with:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [UpdatableTemporalEstimatorToSupervisedAdaptor.Transformer](updatabletemporalestimatortosupervisedadaptor/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedTemporalEstimator Implementations](updatabletemporalestimatortosupervisedadaptor/supervisedtemporalestimator-implementations.md)
- [UpdatableSupervisedTemporalEstimator Implementations](updatabletemporalestimatortosupervisedadaptor/updatablesupervisedtemporalestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SupervisedTemporalEstimator](supervisedtemporalestimator.md)
- [UpdatableSupervisedTemporalEstimator](updatablesupervisedtemporalestimator.md)

## See Also

- [struct UpdatableEstimatorToTemporalAdaptor](updatableestimatortotemporaladaptor.md)
  An updatable temporal estimator wrapping an updatable estimator.
- [struct UpdatableEstimatorToSupervisedAdaptor](updatableestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable estimator as an updatable supervised estimator.
- [struct UpdatableSupervisedEstimatorToTemporalAdaptor](updatablesupervisedestimatortotemporaladaptor.md)
  An updatable supervised temporal estimator wrapping an updatable supervised estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor)*