# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-1nsau.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-45lqe.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-4qkfg.md)
  Composes this updatable estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-5at5c.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-6u48y.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-9oxqt.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkMultiLabelClassifier<Scalar, Label>.Transformer](fullyconnectednetworkmultilabelclassifier/decodewithoptimizer(from:).md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkMultiLabelClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkmultilabelclassifier/encodewithoptimizer(_:to:).md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](fullyconnectednetworkmultilabelclassifier/maketransformer.md)
  Creates a default-initialized fully-connected network multi-label classifier model suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](fullyconnectednetworkmultilabelclassifier/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](fullyconnectednetworkmultilabelclassifier/update(_:with:).md)
- [func update<InputSequence>(inout FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>, with: InputSequence, eventHandler: EventHandler?) async throws](fullyconnectednetworkmultilabelclassifier/update(_:with:eventhandler:).md)
  Updates a fully-connected network multi-label classifier model with a new sequence of examples.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](fullyconnectednetworkmultilabelclassifier/update(_:with:eventhandler:)-72i9r.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](fullyconnectednetworkmultilabelclassifier/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/updatablesupervisedestimator-implementations)*