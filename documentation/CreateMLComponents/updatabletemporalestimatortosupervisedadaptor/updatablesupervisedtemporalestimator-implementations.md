# UpdatableSupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatabletemporalestimatortosupervisedadaptor/appending(_:)-1o6hr.md)
  Composes this updatable supervised temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatabletemporalestimatortosupervisedadaptor/appending(_:)-1qrf8.md)
  Composes this updatable supervised temporal estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatabletemporalestimatortosupervisedadaptor/appending(_:)-30mtf.md)
  Composes this updatable supervised temporal estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](updatabletemporalestimatortosupervisedadaptor/appending(_:)-3of1c.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatabletemporalestimatortosupervisedadaptor/appending(_:)-72v3.md)
  Composes this updatable supervised temporal estimator with another updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](updatabletemporalestimatortosupervisedadaptor/appending(_:)-9z6fo.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](updatabletemporalestimatortosupervisedadaptor/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update<InputSequence, FeatureSequence>(inout Self.Transformer, with: InputSequence) async throws](updatabletemporalestimatortosupervisedadaptor/update(_:with:).md)
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](updatabletemporalestimatortosupervisedadaptor/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimatortosupervisedadaptor/updatablesupervisedtemporalestimator-implementations)*