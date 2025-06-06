# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation>](preprocessingupdatableestimator/adaptedassupervised(annotationtype:)-8t6gv.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](preprocessingupdatableestimator/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](preprocessingupdatableestimator/appending(_:)-2gk1t.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](preprocessingupdatableestimator/appending(_:)-4s2f1.md)
  Composes this updatable estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](preprocessingupdatableestimator/appending(_:)-5fu9k.md)
  Composes this updatable estimator with another updatable estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other>>
](preprocessingupdatableestimator/appending(_:)-97l0s.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](preprocessingupdatableestimator/appending(_:)-9k5ht.md)
  Composes this updatable estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](preprocessingupdatableestimator/appending(_:)-trob.md)
  Composes this updatable estimator with a temporal transformer.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](preprocessingupdatableestimator/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatableestimator/updatableestimator-implementations)*