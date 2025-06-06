# UpdatableSupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-2bwlv.md)
  Composes this updatable supervised temporal estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-4byly.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-4oot9.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-4ux74.md)
  Composes this updatable supervised temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-4wb78.md)
  Composes this updatable supervised temporal estimator with another updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-7jui4.md)
  Composes this updatable supervised temporal estimator with an updatable temporal estimator.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](updatablesupervisedestimatortotemporaladaptor/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence, FeatureSequence>(inout Self.Transformer, with: InputSequence) async throws](updatablesupervisedestimatortotemporaladaptor/update(_:with:).md)
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](updatablesupervisedestimatortotemporaladaptor/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimatortotemporaladaptor/updatablesupervisedtemporalestimator-implementations)*