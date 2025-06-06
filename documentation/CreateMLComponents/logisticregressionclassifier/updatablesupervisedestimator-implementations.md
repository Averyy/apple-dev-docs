# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](logisticregressionclassifier/adaptedastemporal-exas.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-1blzu.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-30xi5.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-47t7f.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-5wy61.md)
  Composes this updatable estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-7ucx1.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-kei5.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LogisticRegressionClassifier<Scalar, Label>.Transformer](logisticregressionclassifier/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(LogisticRegressionClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](logisticregressionclassifier/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> LogisticRegressionClassifier<Scalar, Label>.Transformer](logisticregressionclassifier/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](logisticregressionclassifier/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](logisticregressionclassifier/update(_:with:).md)
- [func update<InputSequence>(inout LogisticRegressionClassifier<Scalar, Label>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](logisticregressionclassifier/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](logisticregressionclassifier/update(_:with:eventhandler:)-w2v0.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](logisticregressionclassifier/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/updatablesupervisedestimator-implementations)*