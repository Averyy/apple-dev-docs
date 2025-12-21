# EstimatorToSupervisedAdaptor

**Framework**: Create ML Components  
**Kind**: struct

An adaptor that exposes an estimator as a supervised estimator.

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
struct EstimatorToSupervisedAdaptor<Estimator, Annotation> where Estimator : Estimator, Annotation : Equatable
```

## Topics

### Creating the adaptor
- [init(Estimator)](estimatortosupervisedadaptor/init(_:).md)
  Creates an estimator adaptor.
### Getting the properties
- [let estimator: Estimator](estimatortosupervisedadaptor/estimator.md)
  The wrapped estimator.
### Encoding and decoding
- [func encode(EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer, to: inout any EstimatorEncoder) throws](estimatortosupervisedadaptor/encode(_:to:).md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](estimatortosupervisedadaptor/decode(from:).md)
  Returns the pre-defined transformer.
### Fitting a transformer
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](estimatortosupervisedadaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples, ignoring the annotations and the validation.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> EstimatorToSupervisedAdaptor<Estimator, Annotation>.Transformer](estimatortosupervisedadaptor/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedEstimator](supervisedestimator.md)

## See Also

- [struct EstimatorToTemporalAdaptor](estimatortotemporaladaptor.md)
  A temporal estimator wrapping an estimator.
- [struct SupervisedEstimatorToTemporalAdaptor](supervisedestimatortotemporaladaptor.md)
  A supervised temporal estimator wrapping a supervised estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortosupervisedadaptor)*