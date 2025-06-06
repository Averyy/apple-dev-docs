# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](preprocessingupdatablesupervisedestimator/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-10j9f.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-4rys8.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-55bjy.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-633gu.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-7dvs.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-83f3r.md)
  Composes this updatable estimator with an updatable estimator.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](preprocessingupdatablesupervisedestimator/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](preprocessingupdatablesupervisedestimator/update(_:with:).md)
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedestimator/update(_:with:eventhandler:)-7ak38.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatablesupervisedestimator/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedestimator/updatablesupervisedestimator-implementations)*