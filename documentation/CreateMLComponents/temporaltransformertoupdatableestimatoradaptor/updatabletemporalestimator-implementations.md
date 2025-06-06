# UpdatableTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableTemporalEstimatorToSupervisedAdaptor<Self, Annotation>](temporaltransformertoupdatableestimatoradaptor/adaptedassupervised(annotationtype:)-6tbi7.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-34y7x.md)
  Composes this updatable temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-38oxe.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-8vr7p.md)
  Composes this updatable temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-9eomm.md)
  Composes this updatable temporal estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-9u468.md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-ifqz.md)
  Composes this updatable temporal estimator with another updatable temporal estimator.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](temporaltransformertoupdatableestimatoradaptor/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor/updatabletemporalestimator-implementations)*