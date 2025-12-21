# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(MultivariateLinearRegressor<Scalar>.Model, to: inout any EstimatorEncoder) throws](multivariatelinearregressor/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> MultivariateLinearRegressor<Scalar>.Model](multivariatelinearregressor/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout MultivariateLinearRegressor<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](multivariatelinearregressor/update(_:with:eventhandler:).md)
  Updates a model with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multivariatelinearregressor/updatablesupervisedestimator-implementations)*