# TabularTransformer Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsEstimator() -> TabularTransformerToEstimatorAdaptor<Self>](columnconcatenator/adaptedasestimator.md)
  Exposes this tabular transformer as a trivial tabular estimator.
- [func adaptedAsUpdatableEstimator() -> TabularTransformerToUpdatableEstimatorAdaptor<Self>](columnconcatenator/adaptedasupdatableestimator.md)
  Exposes this tabular transformer as an updatable tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableTabularEstimator<Self, Other>](columnconcatenator/appending(_:)-2x6d0.md)
  Composes this transformer with an updatable estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>, Other.Annotation>
](columnconcatenator/appending(_:)-323zy.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> ComposedTabularTransformer<Self, Other>](columnconcatenator/appending(_:)-778sy.md)
  Composes this tabular transformer with another tabular transformer.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self, Other.Transformer>>
](columnconcatenator/appending(_:)-8qsij.md)
  Compose this tabular transformer with a tabular estimator.
- [func appending<Other>(Other) -> PreprocessingTabularEstimator<Self, Other>](columnconcatenator/appending(_:)-9nu74.md)
  Composes this transformer with an estimator.
- [func appending<Other>(Other) -> PreprocessingSupervisedTabularEstimator<Self, Other>](columnconcatenator/appending(_:)-r2ia.md)
  Composes this transformer with a supervised tabular estimator.
- [func appending<Other>(Other) -> PreprocessingUpdatableSupervisedTabularEstimator<Self, Other>](columnconcatenator/appending(_:)-w5u1.md)
  Composes this transformer with an updatable supervised estimator.
- [func callAsFunction(DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](columnconcatenator/callasfunction(_:eventhandler:).md)
  Performs the transformation on a single input.
- [func export(to: URL) throws](columnconcatenator/export(to:)-mqpd.md)
  Exports this transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](columnconcatenator/export(to:metadata:)-5lt4h.md)
  Exports this tabular transformer as a CoreML model with userInfo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnconcatenator/tabulartransformer-implementations)*