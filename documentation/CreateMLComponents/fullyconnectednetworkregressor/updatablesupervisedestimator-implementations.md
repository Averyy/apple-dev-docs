# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkRegressor<Scalar>.Transformer](fullyconnectednetworkregressor/decodewithoptimizer(from:).md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkRegressor<Scalar>.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkregressor/encodewithoptimizer(_:to:).md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkRegressorModel<Scalar>](fullyconnectednetworkregressor/maketransformer.md)
  Creates a default-initialized fully connected network regressor model suitable for incremental fitting.
- [func update<InputSequence>(inout FullyConnectedNetworkRegressorModel<Scalar>, with: InputSequence, eventHandler: EventHandler?) async throws](fullyconnectednetworkregressor/update(_:with:eventhandler:).md)
  Updates a fully connected network regressor model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor/updatablesupervisedestimator-implementations)*