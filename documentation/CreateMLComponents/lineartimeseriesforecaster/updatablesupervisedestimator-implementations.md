# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](lineartimeseriesforecaster/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-1ln1.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-2giyc.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-2nkb2.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-3p065.md)
  Composes this updatable estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-6etus.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-7mqkg.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LinearTimeSeriesForecaster<Scalar>.Transformer](lineartimeseriesforecaster/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(LinearTimeSeriesForecaster<Scalar>.Transformer, to: inout any EstimatorEncoder) throws](lineartimeseriesforecaster/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](lineartimeseriesforecaster/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update(inout LinearTimeSeriesForecaster<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](lineartimeseriesforecaster/update(_:with:eventhandler:).md)
  Updates a model with a sequence of features.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](lineartimeseriesforecaster/update(_:with:eventhandler:)-9j2jl.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](lineartimeseriesforecaster/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/updatablesupervisedestimator-implementations)*