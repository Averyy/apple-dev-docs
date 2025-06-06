# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](multivariatelinearregressor/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](multivariatelinearregressor/appending(_:)-297k7.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](multivariatelinearregressor/appending(_:)-4eii.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](multivariatelinearregressor/appending(_:)-6fkty.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](multivariatelinearregressor/appending(_:)-6klxt.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](multivariatelinearregressor/appending(_:)-77vqt.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](multivariatelinearregressor/appending(_:)-8rgjb.md)
  Composes this updatable estimator with an updatable estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](multivariatelinearregressor/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](multivariatelinearregressor/update(_:with:eventhandler:).md)
  Updates a model with a new sequence of examples.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](multivariatelinearregressor/update(_:with:eventhandler:)-5st40.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](multivariatelinearregressor/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/updatablesupervisedestimator-implementations)*