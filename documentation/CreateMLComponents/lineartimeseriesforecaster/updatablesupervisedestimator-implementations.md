# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LinearTimeSeriesForecaster<Scalar>.Transformer](lineartimeseriesforecaster/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(LinearTimeSeriesForecaster<Scalar>.Transformer, to: inout any EstimatorEncoder) throws](lineartimeseriesforecaster/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> LinearTimeSeriesForecaster<Scalar>.Model](lineartimeseriesforecaster/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout LinearTimeSeriesForecaster<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](lineartimeseriesforecaster/update(_:with:eventhandler:).md)
  Updates a model with a sequence of features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/updatablesupervisedestimator-implementations)*