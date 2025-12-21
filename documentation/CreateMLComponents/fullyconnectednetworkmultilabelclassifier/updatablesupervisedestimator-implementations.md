# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkMultiLabelClassifier<Scalar, Label>.Transformer](fullyconnectednetworkmultilabelclassifier/decodewithoptimizer(from:).md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkMultiLabelClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkmultilabelclassifier/encodewithoptimizer(_:to:).md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](fullyconnectednetworkmultilabelclassifier/maketransformer.md)
  Creates a default-initialized fully-connected network multi-label classifier model suitable for incremental fitting.
- [func update<InputSequence>(inout FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>, with: InputSequence, eventHandler: EventHandler?) async throws](fullyconnectednetworkmultilabelclassifier/update(_:with:eventhandler:).md)
  Updates a fully-connected network multi-label classifier model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/updatablesupervisedestimator-implementations)*