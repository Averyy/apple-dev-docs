# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LinearRegressorModel<Scalar>](linearregressor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(LinearRegressorModel<Scalar>, to: inout any EstimatorEncoder) throws](linearregressor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> LinearRegressorModel<Scalar>](linearregressor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout LinearRegressor<Scalar>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](linearregressor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/linearregressor/updatablesupervisedestimator-implementations)*