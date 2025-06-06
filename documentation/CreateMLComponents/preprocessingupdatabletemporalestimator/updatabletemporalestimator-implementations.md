# UpdatableTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableTemporalEstimatorToSupervisedAdaptor<Self, Annotation>](preprocessingupdatabletemporalestimator/adaptedassupervised(annotationtype:)-5oc6x.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](preprocessingupdatabletemporalestimator/appending(_:)-24lyc.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](preprocessingupdatabletemporalestimator/appending(_:)-3q4ci.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](preprocessingupdatabletemporalestimator/appending(_:)-4u45h.md)
  Composes this updatable temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](preprocessingupdatabletemporalestimator/appending(_:)-6khbw.md)
  Composes this updatable temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](preprocessingupdatabletemporalestimator/appending(_:)-6o3uc.md)
  Composes this updatable temporal estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](preprocessingupdatabletemporalestimator/appending(_:)-9rg4h.md)
  Composes this updatable temporal estimator with another updatable temporal estimator.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](preprocessingupdatabletemporalestimator/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator/updatabletemporalestimator-implementations)*