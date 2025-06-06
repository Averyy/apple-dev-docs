# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](fullyconnectednetworkclassifier/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-1tx4p.md)
  Composes this updatable estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-28a85.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-7hd5x.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-7r6p1.md)
  Composes this updatable supervised estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-91zt2.md)
  Composes this updatable supervised estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-94m4x.md)
  Composes this updatable supervised estimator with a temporal transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifier<Scalar, Label>.Transformer](fullyconnectednetworkclassifier/decodewithoptimizer(from:).md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkclassifier/encodewithoptimizer(_:to:).md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkClassifierModel<Scalar, Label>](fullyconnectednetworkclassifier/maketransformer.md)
  Creates a default-initialized fully connected network classifier model suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](fullyconnectednetworkclassifier/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](fullyconnectednetworkclassifier/update(_:with:).md)
- [func update<InputSequence>(inout FullyConnectedNetworkClassifierModel<Scalar, Label>, with: InputSequence, eventHandler: EventHandler?) async throws](fullyconnectednetworkclassifier/update(_:with:eventhandler:).md)
  Updates a fully connected network classifier model with a new sequence of examples.
- [func update<Input>(inout Self.Transformer, with: Input, eventHandler: EventHandler?) async throws](fullyconnectednetworkclassifier/update(_:with:eventhandler:)-ph0.md)
  Updates a transformer on an async sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](fullyconnectednetworkclassifier/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/updatablesupervisedestimator-implementations)*