# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components  
**Role**: API Collection

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TimeSeriesClassifier<Scalar, Label>.Transformer](./decodewithoptimizer%28from%29.md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(TimeSeriesClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](./encodewithoptimizer%28_,to%29.md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> TimeSeriesClassifier<Scalar, Label>.Model](./maketransformer%28%29.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout TimeSeriesClassifier<Scalar, Label>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a model with a new batch of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/updatablesupervisedestimator-implementations)*