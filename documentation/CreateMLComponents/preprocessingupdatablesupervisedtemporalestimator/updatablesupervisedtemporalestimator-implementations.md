# UpdatableSupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-19nh.md)
  Composes this updatable supervised temporal estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-4df5k.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-5es09.md)
  Composes this updatable supervised temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-7hvt2.md)
  Composes this updatable supervised temporal estimator with another updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-tkmb.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-xq3u.md)
  Composes this updatable supervised temporal estimator with an updatable temporal estimator.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](preprocessingupdatablesupervisedtemporalestimator/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence, FeatureSequence>(inout Self.Transformer, with: InputSequence) async throws](preprocessingupdatablesupervisedtemporalestimator/update(_:with:).md)
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatablesupervisedtemporalestimator/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator/updatablesupervisedtemporalestimator-implementations)*