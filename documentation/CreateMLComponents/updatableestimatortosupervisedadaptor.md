# UpdatableEstimatorToSupervisedAdaptor

**Framework**: Create ML Components  
**Kind**: struct

An adaptor that exposes an updatable estimator as an updatable supervised estimator.

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
struct UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation> where Estimator : UpdatableEstimator, Annotation : Equatable
```

## Topics

### Creating an adaptor
- [init(Estimator)](updatableestimatortosupervisedadaptor/init(_:).md)
  Creates an estimator adaptor.
### Getting the estimator
- [let estimator: Estimator](updatableestimatortosupervisedadaptor/estimator.md)
  The wrapped estimator.
### Encoding and decoding
- [func encode(UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](updatableestimatortosupervisedadaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatableestimatortosupervisedadaptor/decode(from:).md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](updatableestimatortosupervisedadaptor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatableestimatortosupervisedadaptor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer.
### Fitting and Updating
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatableestimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples, ignoring the annotations and the validation.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](updatableestimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func makeTransformer() -> Estimator.Transformer](updatableestimatortosupervisedadaptor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Estimator.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatableestimatortosupervisedadaptor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, Validation>(inout Estimator.Transformer, with: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws](updatableestimatortosupervisedadaptor/update(_:with:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedEstimator](supervisedestimator.md)
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)

## See Also

- [struct UpdatableEstimatorToTemporalAdaptor](updatableestimatortotemporaladaptor.md)
  An updatable temporal estimator wrapping an updatable estimator.
- [struct UpdatableSupervisedEstimatorToTemporalAdaptor](updatablesupervisedestimatortotemporaladaptor.md)
  An updatable supervised temporal estimator wrapping an updatable supervised estimator.
- [struct UpdatableTemporalEstimatorToSupervisedAdaptor](updatabletemporalestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable temporal estimator as an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortosupervisedadaptor)*