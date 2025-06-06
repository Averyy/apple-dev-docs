# TabularTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TabularTransformerToEstimatorAdaptor<Self>](treeregressormodel/adaptedasestimator.md)
  Exposes this tabular transformer as a trivial tabular estimator.
- [func adaptedAsUpdatableEstimator() -> TabularTransformerToUpdatableEstimatorAdaptor<Self>](treeregressormodel/adaptedasupdatableestimator.md)
  Exposes this tabular transformer as an updatable tabular estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTabularEstimator<Self, Other>](treeregressormodel/appending(_:)-2hoij.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTabularEstimator<Self, Other>](treeregressormodel/appending(_:)-69hs1.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> ComposedTabularTransformer<Self, Other>](treeregressormodel/appending(_:)-6ykdn.md)
  Composes this tabular transformer with another tabular transformer.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>, Other.Annotation>
](treeregressormodel/appending(_:)-8iy5y.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other>](treeregressormodel/appending(_:)-8ubf0.md)
  Composes this transformer with an updatable supervised estimator.
- [func appending<Other>(Other) -> PreprocessingTabularEstimator<Self, Other>](treeregressormodel/appending(_:)-8zo52.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>>
](treeregressormodel/appending(_:)-9rqjv.md)
  Compose this tabular transformer with a tabular estimator.
- [func callAsFunction(DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](treeregressormodel/callasfunction(_:eventhandler:).md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](treeregressormodel/export(to:)-hzwj.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](treeregressormodel/export(to:metadata:)-3a066.md)
  Exports this tabular transformer as a CoreML model with userInfo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/treeregressormodel/tabulartransformer-implementations)*