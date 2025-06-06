# TabularTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TabularTransformerToEstimatorAdaptor<Self>](columnselectortransformer/adaptedasestimator.md)
  Exposes this tabular transformer as a trivial tabular estimator.
- [func adaptedAsUpdatableEstimator() -> TabularTransformerToUpdatableEstimatorAdaptor<Self>](columnselectortransformer/adaptedasupdatableestimator.md)
  Exposes this tabular transformer as an updatable tabular estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTabularEstimator<Self, Other>](columnselectortransformer/appending(_:)-1mbgh.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> PreprocessingTabularEstimator<Self, Other>](columnselectortransformer/appending(_:)-4p4wk.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>>
](columnselectortransformer/appending(_:)-62baz.md)
  Compose this tabular transformer with a tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other>](columnselectortransformer/appending(_:)-6cx6o.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>, Other.Annotation>
](columnselectortransformer/appending(_:)-77dsb.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTabularEstimator<Self, Other>](columnselectortransformer/appending(_:)-9lixx.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTabularTransformer<Self, Other>](columnselectortransformer/appending(_:)-pzb6.md)
  Composes this tabular transformer with another tabular transformer.
- [func callAsFunction(DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](columnselectortransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](columnselectortransformer/export(to:)-6hoh1.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](columnselectortransformer/export(to:metadata:)-9bpdl.md)
  Exports this tabular transformer as a CoreML model with userInfo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselectortransformer/tabulartransformer-implementations)*