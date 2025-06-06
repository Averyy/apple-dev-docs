# TabularTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TabularTransformerToEstimatorAdaptor<Self>](treeclassifiermodel/adaptedasestimator.md)
  Exposes this tabular transformer as a trivial tabular estimator.
- [func adaptedAsUpdatableEstimator() -> TabularTransformerToUpdatableEstimatorAdaptor<Self>](treeclassifiermodel/adaptedasupdatableestimator.md)
  Exposes this tabular transformer as an updatable tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>>
](treeclassifiermodel/appending(_:)-2wik9.md)
  Compose this tabular transformer with a tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTabularEstimator<Self, Other>](treeclassifiermodel/appending(_:)-4ykrs.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> PreprocessingTabularEstimator<Self, Other>](treeclassifiermodel/appending(_:)-5441o.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other>](treeclassifiermodel/appending(_:)-63pf9.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTabularEstimator<Self, Other>](treeclassifiermodel/appending(_:)-7qn8t.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>, Other.Annotation>
](treeclassifiermodel/appending(_:)-8wepu.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> ComposedTabularTransformer<Self, Other>](treeclassifiermodel/appending(_:)-9wivc.md)
  Composes this tabular transformer with another tabular transformer.
- [func callAsFunction(DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](treeclassifiermodel/callasfunction(_:eventhandler:).md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](treeclassifiermodel/export(to:)-8weiu.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](treeclassifiermodel/export(to:metadata:)-3jw0c.md)
  Exports this tabular transformer as a CoreML model with userInfo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/treeclassifiermodel/tabulartransformer-implementations)*