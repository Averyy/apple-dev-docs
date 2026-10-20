# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LinearTimeSeriesForecaster<Scalar>.Transformer](./decodewithoptimizer%28from%29.md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(LinearTimeSeriesForecaster<Scalar>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> LinearTimeSeriesForecaster<Scalar>.Model](./maketransformer%28%29.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout LinearTimeSeriesForecaster<Scalar>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>>, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a model with a sequence of features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/updatablesupervisedestimator-implementations)*