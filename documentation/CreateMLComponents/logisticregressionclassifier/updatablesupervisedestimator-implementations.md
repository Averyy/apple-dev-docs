# UpdatableSupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> LogisticRegressionClassifier<Scalar, Label>.Transformer](logisticregressionclassifier/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(LogisticRegressionClassifier<Scalar, Label>.Transformer, to: inout any EstimatorEncoder) throws](logisticregressionclassifier/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> LogisticRegressionClassifier<Scalar, Label>.Transformer](logisticregressionclassifier/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout LogisticRegressionClassifier<Scalar, Label>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](logisticregressionclassifier/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/updatablesupervisedestimator-implementations)*