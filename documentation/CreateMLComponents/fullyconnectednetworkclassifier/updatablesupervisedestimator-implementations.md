# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifier<Scalar, Label>.Transformer](./decodewithoptimizer%28from%29.md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkClassifierModel<Scalar, Label>](./maketransformer%28%29.md)
  Creates a default-initialized fully connected network classifier model suitable for incremental fitting.
- [func update<InputSequence>(inout FullyConnectedNetworkClassifierModel<Scalar, Label>, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a fully connected network classifier model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/updatablesupervisedestimator-implementations)*