# TabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](preprocessingupdatabletabularestimator/adaptedassupervised(annotationcolumnid:)-6nic0.md)
  Exposes this tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](preprocessingupdatabletabularestimator/appending(_:)-32sb3.md)
  Compose this tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](preprocessingupdatabletabularestimator/appending(_:)-397om.md)
  Compose this tabular estimator with another tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](preprocessingupdatabletabularestimator/appending(_:)-71jth.md)
  Composes this tabular estimator with a supervised tabular estimator.
- [func fitted(to: DataFrame) async throws -> Self.Transformer](preprocessingupdatabletabularestimator/fitted(to:)-1tqp1.md)
- [func fitted(to: DataFrame) async throws -> Self.Transformer](preprocessingupdatabletabularestimator/fitted(to:)-9ci9.md)
- [func read(from: URL) throws -> Self.Transformer](preprocessingupdatabletabularestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatabletabularestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletabularestimator/tabularestimator-implementations)*