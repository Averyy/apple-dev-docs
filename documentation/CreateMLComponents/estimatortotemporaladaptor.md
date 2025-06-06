# EstimatorToTemporalAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A temporal estimator wrapping an estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct EstimatorToTemporalAdaptor<Base> where Base : Estimator
```

## Topics

### Creating the estimator
- [init(Base)](estimatortotemporaladaptor/init(_:).md)
  Creates a temporal estimator from an estimator.
### Encoding and decoding
- [func encode(EstimatorToTemporalAdaptor<Base>.Transformer, to: inout any EstimatorEncoder) throws](estimatortotemporaladaptor/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> EstimatorToTemporalAdaptor<Base>.Transformer](estimatortotemporaladaptor/decode(from:).md)
  Decodes the transformer.
### Fitting a transformer
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> EstimatorToTemporalAdaptor<Base>.Transformer](estimatortotemporaladaptor/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [EstimatorToTemporalAdaptor.Input](estimatortotemporaladaptor/input.md)
  The input type.
- [EstimatorToTemporalAdaptor.Output](estimatortotemporaladaptor/output.md)
  The output type.
- [EstimatorToTemporalAdaptor.Transformer](estimatortotemporaladaptor/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [TemporalEstimator Implementations](estimatortotemporaladaptor/temporalestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [TemporalEstimator](temporalestimator.md)

## See Also

- [struct EstimatorToSupervisedAdaptor](estimatortosupervisedadaptor.md)
  An adaptor that exposes an estimator as a supervised estimator.
- [struct SupervisedEstimatorToTemporalAdaptor](supervisedestimatortotemporaladaptor.md)
  A supervised temporal estimator wrapping a supervised estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortotemporaladaptor)*