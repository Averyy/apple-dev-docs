# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifier<Scalar, Label>.Transformer](fullyconnectednetworkclassifier/decodewithoptimizer(from:).md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkclassifier/encodewithoptimizer(_:to:).md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkClassifierModel<Scalar, Label>](fullyconnectednetworkclassifier/maketransformer.md)
  Creates a default-initialized fully connected network classifier model suitable for incremental fitting.
- [func update<InputSequence>(inout FullyConnectedNetworkClassifierModel<Scalar, Label>, with: InputSequence, eventHandler: EventHandler?) async throws](fullyconnectednetworkclassifier/update(_:with:eventhandler:).md)
  Updates a fully connected network classifier model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/updatablesupervisedestimator-implementations)*