# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](boostedtreeclassifier/appending(_:)-2oc3r.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](boostedtreeclassifier/appending(_:)-70505.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](boostedtreeclassifier/appending(_:)-7bot0.md)
  Composes this supervised tabular estimator with an updatable tabular estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TreeClassifierModel<Label>](boostedtreeclassifier/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(TreeClassifierModel<Label>, to: inout any EstimatorEncoder) throws](boostedtreeclassifier/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> TreeClassifierModel<Label>](boostedtreeclassifier/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](boostedtreeclassifier/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update(inout Self.Transformer, with: DataFrame) async throws](boostedtreeclassifier/update(_:with:).md)
- [func update(inout TreeClassifierModel<Label>, with: DataFrame, eventHandler: EventHandler?) async throws](boostedtreeclassifier/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](boostedtreeclassifier/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeclassifier/updatablesupervisedtabularestimator-implementations)*