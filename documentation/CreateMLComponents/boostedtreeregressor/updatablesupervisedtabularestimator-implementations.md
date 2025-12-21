# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TreeRegressorModel](boostedtreeregressor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(TreeRegressorModel, to: inout any EstimatorEncoder) throws](boostedtreeregressor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> TreeRegressorModel](boostedtreeregressor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout TreeRegressorModel, with: DataFrame, eventHandler: EventHandler?) async throws](boostedtreeregressor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor/updatablesupervisedtabularestimator-implementations)*