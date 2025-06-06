# UpdatableEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation>](transformertoupdatableestimatoradaptor/adaptedassupervised(annotationtype:)-v89g.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](transformertoupdatableestimatoradaptor/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](transformertoupdatableestimatoradaptor/appending(_:)-1tac0.md)
  Composes this updatable estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other>>
](transformertoupdatableestimatoradaptor/appending(_:)-5481g.md)
  Composes this updatable estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](transformertoupdatableestimatoradaptor/appending(_:)-6jcs5.md)
  Composes this updatable estimator with an updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](transformertoupdatableestimatoradaptor/appending(_:)-80zmw.md)
  Composes this updatable estimator with a temporal transformer.
- [func appending<Other>(Other) -> some UpdatableTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](transformertoupdatableestimatoradaptor/appending(_:)-87bf3.md)
  Composes this updatable estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](transformertoupdatableestimatoradaptor/appending(_:)-8ko9p.md)
  Composes this updatable estimator with another updatable estimator.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](transformertoupdatableestimatoradaptor/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/updatableestimator-implementations)*