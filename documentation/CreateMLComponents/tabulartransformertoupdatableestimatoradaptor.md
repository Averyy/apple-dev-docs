# TabularTransformerToUpdatableEstimatorAdaptor

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

An updatable tabular estimator that always returns a predefined transformer.

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
struct TabularTransformerToUpdatableEstimatorAdaptor<Transformer> where Transformer : TabularTransformer
```

## Topics

### Creating an estimator
- [init(Transformer)](./tabulartransformertoupdatableestimatoradaptor/init%28_%29.md)
  Creates an updatable tabular estimator from a tabular transformer.
### Creating a default transformer
- [func makeTransformer() -> Transformer](./tabulartransformertoupdatableestimatoradaptor/maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
### Getting the transformer
- [let transformer: Transformer](./tabulartransformertoupdatableestimatoradaptor/transformer.md)
  A pre-defined transformer.
### Encoding and decoding
- [func encode(Transformer, to: inout any EstimatorEncoder) throws](./tabulartransformertoupdatableestimatoradaptor/encode%28_,to%29.md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Transformer](./tabulartransformertoupdatableestimatoradaptor/decode%28from%29.md)
  Returns the pre-defined transformer.
- [func encodeWithOptimizer(Transformer, to: inout any EstimatorEncoder) throws](./tabulartransformertoupdatableestimatoradaptor/encodewithoptimizer%28_,to%29.md)
  Does nothing since this estimator uses a pre-defined transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Transformer](./tabulartransformertoupdatableestimatoradaptor/decodewithoptimizer%28from%29.md)
  Returns the pre-defined transformer.
### Fitting
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> Transformer](./tabulartransformertoupdatableestimatoradaptor/fitted%28to,eventhandler%29.md)
  Returns the pre-defined transformer.
- [func update(inout Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](./tabulartransformertoupdatableestimatoradaptor/update%28_,with,eventhandler%29.md)
  Does nothing since this estimator uses a pre-defined transformer.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TabularEstimator](./tabularestimator.md)
- [UpdatableTabularEstimator](./updatabletabularestimator.md)

## See Also

### Tabular adaptors
- [struct TabularEstimatorToSupervisedAdaptor](./tabularestimatortosupervisedadaptor.md)
  An adaptor that exposes a tabular estimator as a tabular supervised estimator.
- [struct TabularTransformerToEstimatorAdaptor](./tabulartransformertoestimatoradaptor.md)
  A tabular estimator that always returns a predefined tabular transformer.
- [struct UpdatableTabularEstimatorToSupervisedAdaptor](./updatabletabularestimatortosupervisedadaptor.md)
  An adaptor that exposes an updatable tabular estimator as an updatable supervised tabular estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoupdatableestimatoradaptor)*