# UpdatableTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> UpdatableTabularEstimatorToSupervisedAdaptor<Self, Annotation>](preprocessingupdatabletabularestimator/adaptedassupervised(annotationcolumnid:)-90xpl.md)
  Exposes this updatable tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](preprocessingupdatabletabularestimator/appending(_:)-3aagb.md)
  Composes this updatable tabular estimator with an updatable supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](preprocessingupdatabletabularestimator/appending(_:)-4p7u0.md)
  Composes this updatable tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](preprocessingupdatabletabularestimator/appending(_:)-8daxn.md)
  Composes this updatable tabular estimator with another updatable tabular estimator.
- [func update(inout Self.Transformer, with: DataFrame) async throws](preprocessingupdatabletabularestimator/update(_:with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletabularestimator/updatabletabularestimator-implementations)*