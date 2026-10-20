# UpdatableSupervisedEstimatorToTemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An updatable supervised temporal estimator wrapping an updatable supervised estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
struct UpdatableSupervisedEstimatorToTemporalAdaptor<Base> where Base : UpdatableSupervisedEstimator, Base.Annotation : Sendable
```

## Topics

### Creating an adaptor
- [init(Base)](./updatablesupervisedestimatortotemporaladaptor/init%28_%29.md)
  Creates a temporal supervised estimator from a supervised estimator.
### Encoding and decoding
- [func encode(UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./updatablesupervisedestimatortotemporaladaptor/encode%28_,to%29.md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./updatablesupervisedestimatortotemporaladaptor/decode%28from%29.md)
  Decodes the transformer.
- [func encodeWithOptimizer(UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./updatablesupervisedestimatortotemporaladaptor/encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./updatablesupervisedestimatortotemporaladaptor/decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer with a decoder.
### Fitting and updating
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./updatablesupervisedestimatortotemporaladaptor/fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./updatablesupervisedestimatortotemporaladaptor/fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func makeTransformer() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./updatablesupervisedestimatortotemporaladaptor/maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout UpdatableSupervisedEstimatorToTemporalAdaptor<Base>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./updatablesupervisedestimatortotemporaladaptor/update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.
- [UpdatableSupervisedEstimatorToTemporalAdaptor.Annotation](./updatablesupervisedestimatortotemporaladaptor/annotation.md)
  The annotation type.
- [UpdatableSupervisedEstimatorToTemporalAdaptor.Input](./updatablesupervisedestimatortotemporaladaptor/input.md)
  The input type.
- [UpdatableSupervisedEstimatorToTemporalAdaptor.Output](./updatablesupervisedestimatortotemporaladaptor/output.md)
  The output type.
- [UpdatableSupervisedEstimatorToTemporalAdaptor.Transformer](./updatablesupervisedestimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SupervisedTemporalEstimator](./supervisedtemporalestimator.md)
- [UpdatableSupervisedTemporalEstimator](./updatablesupervisedtemporalestimator.md)

## See Also

### Updatable adaptors
- [struct UpdatableEstimatorToTemporalAdaptor](./updatableestimatortotemporaladaptor.md)
  An updatable temporal estimator wrapping an updatable estimator.
- [struct UpdatableEstimatorToSupervisedAdaptor](./updatableestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable estimator as an updatable supervised estimator.
- [struct UpdatableTemporalEstimatorToSupervisedAdaptor](./updatabletemporalestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable temporal estimator as an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimatortotemporaladaptor)*