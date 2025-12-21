# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TimeSeriesClassifier<Scalar, Label>.Transformer](timeseriesclassifier/decodewithoptimizer(from:).md)
  Reads the encoded model and optimizer with a decoder.
- [func encodeWithOptimizer(TimeSeriesClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](timeseriesclassifier/encodewithoptimizer(_:to:).md)
  Encodes the model and optimizer to an encoder.
- [func makeTransformer() -> TimeSeriesClassifier<Scalar, Label>.Model](timeseriesclassifier/maketransformer.md)
  Creates a default-initialized model suitable for incremental fitting.
- [func update(inout TimeSeriesClassifier<Scalar, Label>.Model, with: some Sequence<AnnotatedFeature<MLShapedArray<Scalar>, Label>>, eventHandler: EventHandler?) async throws](timeseriesclassifier/update(_:with:eventhandler:).md)
  Updates a model with a new batch of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/updatablesupervisedestimator-implementations)*