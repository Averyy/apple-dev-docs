# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](linearregressor/adaptedastemporal-9o3qw.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](linearregressor/appending(_:)-1g1lh.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](linearregressor/appending(_:)-1psmo.md)
  Composes this updatable estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](linearregressor/appending(_:)-2jrch.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](linearregressor/appending(_:)-33g0.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](linearregressor/appending(_:)-4netb.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](linearregressor/appending(_:)-80uig.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LinearRegressorModel<Scalar>](linearregressor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(LinearRegressorModel<Scalar>, to: inout any EstimatorEncoder) throws](linearregressor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> LinearRegressorModel<Scalar>](linearregressor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](linearregressor/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](linearregressor/update(_:with:).md)
- [func update<InputSequence>(inout LinearRegressor<Scalar>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](linearregressor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](linearregressor/update(_:with:eventhandler:)-4to11.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](linearregressor/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/updatablesupervisedestimator-implementations)*