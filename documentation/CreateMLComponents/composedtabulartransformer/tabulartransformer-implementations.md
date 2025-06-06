# TabularTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TabularTransformerToEstimatorAdaptor<Self>](composedtabulartransformer/adaptedasestimator.md)
  Exposes this tabular transformer as a trivial tabular estimator.
- [func adaptedAsUpdatableEstimator() -> TabularTransformerToUpdatableEstimatorAdaptor<Self>](composedtabulartransformer/adaptedasupdatableestimator.md)
  Exposes this tabular transformer as an updatable tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other>](composedtabulartransformer/appending(_:)-1rzuw.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTabularEstimator<Self, Other>](composedtabulartransformer/appending(_:)-36r22.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> ComposedTabularTransformer<Self, Other>](composedtabulartransformer/appending(_:)-610co.md)
  Composes this tabular transformer with another tabular transformer.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>>
](composedtabulartransformer/appending(_:)-66xpl.md)
  Compose this tabular transformer with a tabular estimator.
- [func appending<Other>(Other) -> PreprocessingTabularEstimator<Self, Other>](composedtabulartransformer/appending(_:)-6kky4.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTabularEstimator<Self, Other>](composedtabulartransformer/appending(_:)-7gyjb.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>, Other.Annotation>
](composedtabulartransformer/appending(_:)-8jsqd.md)
  Composes this transformer with a supervised tabular estimator.
- [func callAsFunction(DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](composedtabulartransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](composedtabulartransformer/export(to:)-5wrte.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](composedtabulartransformer/export(to:metadata:)-3kwx7.md)
  Exports this tabular transformer as a CoreML model with userInfo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/composedtabulartransformer/tabulartransformer-implementations)*