# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkMultiLabelClassifier<Scalar, Label>.Transformer](./decodewithoptimizer%28from%29.md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkMultiLabelClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](./maketransformer%28%29.md)
  Creates a default-initialized fully-connected network multi-label classifier model suitable for incremental fitting.
- [func update<InputSequence>(inout FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a fully-connected network multi-label classifier model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/updatablesupervisedestimator-implementations)*