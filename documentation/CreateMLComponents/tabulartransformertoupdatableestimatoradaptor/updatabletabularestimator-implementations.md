# UpdatableTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> UpdatableTabularEstimatorToSupervisedAdaptor<Self, Annotation>](tabulartransformertoupdatableestimatoradaptor/adaptedassupervised(annotationcolumnid:)-84bvn.md)
  Exposes this updatable tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](tabulartransformertoupdatableestimatoradaptor/appending(_:)-4ihs6.md)
  Composes this updatable tabular estimator with an updatable supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](tabulartransformertoupdatableestimatoradaptor/appending(_:)-7oplf.md)
  Composes this updatable tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](tabulartransformertoupdatableestimatoradaptor/appending(_:)-93tdk.md)
  Composes this updatable tabular estimator with another updatable tabular estimator.
- [func update(inout Self.Transformer, with: DataFrame) async throws](tabulartransformertoupdatableestimatoradaptor/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoupdatableestimatoradaptor/updatabletabularestimator-implementations)*