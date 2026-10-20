# SupervisedEstimatorToTemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A supervised temporal estimator wrapping a supervised estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
struct SupervisedEstimatorToTemporalAdaptor<Base> where Base : SupervisedEstimator, Base.Annotation : Sendable
```

## Topics

### Creating an estimator
- [init(Base)](./supervisedestimatortotemporaladaptor/init%28_%29.md)
  Creates a temporal supervised estimator from a supervised estimator.
### Encoding and decoding
- [func encode(SupervisedEstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](./supervisedestimatortotemporaladaptor/encode%28_,to%29.md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./supervisedestimatortotemporaladaptor/decode%28from%29.md)
  Decodes the transformer.
### Fitting
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./supervisedestimatortotemporaladaptor/fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> SupervisedEstimatorToTemporalAdaptor<Base>.Transformer](./supervisedestimatortotemporaladaptor/fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [SupervisedEstimatorToTemporalAdaptor.Annotation](./supervisedestimatortotemporaladaptor/annotation.md)
  The annotation type.
- [SupervisedEstimatorToTemporalAdaptor.Input](./supervisedestimatortotemporaladaptor/input.md)
  The input type.
- [SupervisedEstimatorToTemporalAdaptor.Output](./supervisedestimatortotemporaladaptor/output.md)
  The output type.
- [SupervisedEstimatorToTemporalAdaptor.Transformer](./supervisedestimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SupervisedTemporalEstimator](./supervisedtemporalestimator.md)

## See Also

### Estimator adaptors
- [struct EstimatorToSupervisedAdaptor](./estimatortosupervisedadaptor.md)
  An adaptor that exposes an estimator as a supervised estimator.
- [struct EstimatorToTemporalAdaptor](./estimatortotemporaladaptor.md)
  A temporal estimator wrapping an estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor)*