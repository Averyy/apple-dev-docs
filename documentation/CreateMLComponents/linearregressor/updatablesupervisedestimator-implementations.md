# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LinearRegressorModel<Scalar>](./decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(LinearRegressorModel<Scalar>, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> LinearRegressorModel<Scalar>](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout LinearRegressor<Scalar>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/updatablesupervisedestimator-implementations)*