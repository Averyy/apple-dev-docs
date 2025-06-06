# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](boostedtreeregressor/appending(_:)-6n1ry.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](boostedtreeregressor/appending(_:)-j0rd.md)
  Composes this supervised tabular estimator with an updatable tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](boostedtreeregressor/appending(_:)-uyi7.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> TreeRegressorModel](boostedtreeregressor/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(TreeRegressorModel, to: inout any EstimatorEncoder) throws](boostedtreeregressor/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> TreeRegressorModel](boostedtreeregressor/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](boostedtreeregressor/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update(inout Self.Transformer, with: DataFrame) async throws](boostedtreeregressor/update(_:with:).md)
- [func update(inout TreeRegressorModel, with: DataFrame, eventHandler: EventHandler?) async throws](boostedtreeregressor/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](boostedtreeregressor/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor/updatablesupervisedtabularestimator-implementations)*