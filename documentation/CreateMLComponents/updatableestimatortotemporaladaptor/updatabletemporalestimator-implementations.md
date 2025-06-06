# UpdatableTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableTemporalEstimatorToSupervisedAdaptor<Self, Annotation>](updatableestimatortotemporaladaptor/adaptedassupervised(annotationtype:)-3joto.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](updatableestimatortotemporaladaptor/appending(_:)-19jnk.md)
  Composes this updatable temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](updatableestimatortotemporaladaptor/appending(_:)-39215.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](updatableestimatortotemporaladaptor/appending(_:)-3nsww.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](updatableestimatortotemporaladaptor/appending(_:)-47whk.md)
  Composes this updatable temporal estimator with another updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](updatableestimatortotemporaladaptor/appending(_:)-59ras.md)
  Composes this updatable temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](updatableestimatortotemporaladaptor/appending(_:)-g6tb.md)
  Composes this updatable temporal estimator with a temporal transformer.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](updatableestimatortotemporaladaptor/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/updatabletemporalestimator-implementations)*