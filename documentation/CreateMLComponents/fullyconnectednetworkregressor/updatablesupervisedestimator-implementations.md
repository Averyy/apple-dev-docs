# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkRegressor<Scalar>.Transformer](./decodewithoptimizer%28from%29.md)
  Decodes a previously fitted transformer with an optimizer.
- [func encodeWithOptimizer(FullyConnectedNetworkRegressor<Scalar>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes a fitted transformer with an optimizer.
- [func makeTransformer() -> FullyConnectedNetworkRegressorModel<Scalar>](./maketransformer%28%29.md)
  Creates a default-initialized fully connected network regressor model suitable for incremental fitting.
- [func update<InputSequence>(inout FullyConnectedNetworkRegressorModel<Scalar>, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a fully connected network regressor model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor/updatablesupervisedestimator-implementations)*