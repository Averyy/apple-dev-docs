# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](timeseriesclassifier/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-1x8m3.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](timeseriesclassifier/appending(_:)-6ubru.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-88vjq.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-8kt0e.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-eimw.md)
  Composes this updatable estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](timeseriesclassifier/appending(_:)-sgbn.md)
  Composes this updatable estimator with a transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TimeSeriesClassifier<Scalar, Label>.Transformer](timeseriesclassifier/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(TimeSeriesClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](timeseriesclassifier/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> TimeSeriesClassifier<Scalar, Label>.Model](timeseriesclassifier/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](timeseriesclassifier/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](timeseriesclassifier/update(_:with:).md)
- [func update(inout TimeSeriesClassifier<Scalar, Label>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler?) async throws](timeseriesclassifier/update(_:with:eventhandler:).md)
  Updates a model with a new batch of examples.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](timeseriesclassifier/update(_:with:eventhandler:)-9uoi7.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](timeseriesclassifier/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/updatablesupervisedestimator-implementations)*