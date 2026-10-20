# UpdatableEstimatorToTemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An updatable temporal estimator wrapping an updatable estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
struct UpdatableEstimatorToTemporalAdaptor<Base> where Base : UpdatableEstimator
```

## Topics

### Creating an adaptor
- [init(Base)](./updatableestimatortotemporaladaptor/init%28_%29.md)
  Creates a temporal estimator from an estimator.
### Encoding and decoding
- [func encode(UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./updatableestimatortotemporaladaptor/encode%28_,to%29.md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](./updatableestimatortotemporaladaptor/decode%28from%29.md)
  Decodes the transformer.
- [func encodeWithOptimizer(UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./updatableestimatortotemporaladaptor/encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](./updatableestimatortotemporaladaptor/decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer with a decoder.
### Fitting and updating
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](./updatableestimatortotemporaladaptor/fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func makeTransformer() -> UpdatableEstimatorToTemporalAdaptor<Base>.Transformer](./updatableestimatortotemporaladaptor/maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout UpdatableEstimatorToTemporalAdaptor<Base>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./updatableestimatortotemporaladaptor/update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.
- [UpdatableEstimatorToTemporalAdaptor.Input](./updatableestimatortotemporaladaptor/input.md)
  The input type.
- [UpdatableEstimatorToTemporalAdaptor.Output](./updatableestimatortotemporaladaptor/output.md)
  The output type.
- [UpdatableEstimatorToTemporalAdaptor.Transformer](./updatableestimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TemporalEstimator](./temporalestimator.md)
- [UpdatableTemporalEstimator](./updatabletemporalestimator.md)

## See Also

### Updatable adaptors
- [struct UpdatableEstimatorToSupervisedAdaptor](./updatableestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable estimator as an updatable supervised estimator.
- [struct UpdatableSupervisedEstimatorToTemporalAdaptor](./updatablesupervisedestimatortotemporaladaptor.md)
  An updatable supervised temporal estimator wrapping an updatable supervised estimator.
- [struct UpdatableTemporalEstimatorToSupervisedAdaptor](./updatabletemporalestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable temporal estimator as an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor)*