# TabularTransformerToEstimatorAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A tabular estimator that always returns a predefined tabular transformer.

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
struct TabularTransformerToEstimatorAdaptor<Transformer> where Transformer : TabularTransformer
```

## Topics

### Creating an estimator
- [init(Transformer)](tabulartransformertoestimatoradaptor/init(_:).md)
  Creates a trivial tabular estimator.
### Getting the transformer
- [let transformer: Transformer](tabulartransformertoestimatoradaptor/transformer.md)
  A pre-defined tabular transformer.
### Encoding and decoding
- [func encode(Transformer, to: inout any EstimatorEncoder) throws](tabulartransformertoestimatoradaptor/encode(_:to:).md)
  Does nothing since this tabular estimator uses a pre-defined tabular transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](tabulartransformertoestimatoradaptor/decode(from:).md)
  Returns the pre-defined tabular transformer.
### Fitting
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> Transformer](tabulartransformertoestimatoradaptor/fitted(to:eventhandler:).md)
  Returns the pre-defined tabular transformer.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabularEstimator](tabularestimator.md)

## See Also

- [struct TabularEstimatorToSupervisedAdaptor](tabularestimatortosupervisedadaptor.md)
  An adaptor that exposes a tabular estimator as a tabular supervised estimator.
- [struct TabularTransformerToUpdatableEstimatorAdaptor](tabulartransformertoupdatableestimatoradaptor.md)
  An updatable tabular estimator that always returns a predefined transformer.
- [struct UpdatableTabularEstimatorToSupervisedAdaptor](updatabletabularestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable tabular estimator as an updatable supervised tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoestimatoradaptor)*