# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TreeClassifierModel<Label>](boostedtreeclassifier/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(TreeClassifierModel<Label>, to: inout any EstimatorEncoder) throws](boostedtreeclassifier/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> TreeClassifierModel<Label>](boostedtreeclassifier/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout TreeClassifierModel<Label>, with: DataFrame, eventHandler: EventHandler?) async throws](boostedtreeclassifier/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier/updatablesupervisedtabularestimator-implementations)*