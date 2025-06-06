# TabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](preprocessingtabularestimator/adaptedassupervised(annotationcolumnid:).md)
  Exposes this tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](preprocessingtabularestimator/appending(_:)-2vdot.md)
  Composes this tabular estimator with a supervised tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](preprocessingtabularestimator/appending(_:)-5w500.md)
  Compose this tabular estimator with another tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](preprocessingtabularestimator/appending(_:)-8unz6.md)
  Compose this tabular estimator with a tabular transformer.
- [func fitted(to: DataFrame) async throws -> Self.Transformer](preprocessingtabularestimator/fitted(to:)-6q5mh.md)
- [func fitted(to: DataFrame) async throws -> Self.Transformer](preprocessingtabularestimator/fitted(to:)-91004.md)
- [func read(from: URL) throws -> Self.Transformer](preprocessingtabularestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingtabularestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtabularestimator/tabularestimator-implementations)*