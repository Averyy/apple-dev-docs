# TabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](tabulartransformertoupdatableestimatoradaptor/adaptedassupervised(annotationcolumnid:)-1nq9a.md)
  Exposes this tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](tabulartransformertoupdatableestimatoradaptor/appending(_:)-3911f.md)
  Composes this tabular estimator with a supervised tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](tabulartransformertoupdatableestimatoradaptor/appending(_:)-828kb.md)
  Compose this tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](tabulartransformertoupdatableestimatoradaptor/appending(_:)-wh1i.md)
  Compose this tabular estimator with another tabular estimator.
- [func fitted(to: DataFrame) async throws -> Self.Transformer](tabulartransformertoupdatableestimatoradaptor/fitted(to:)-5akb5.md)
- [func fitted(to: DataFrame) async throws -> Self.Transformer](tabulartransformertoupdatableestimatoradaptor/fitted(to:)-9jw8r.md)
- [func read(from: URL) throws -> Self.Transformer](tabulartransformertoupdatableestimatoradaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](tabulartransformertoupdatableestimatoradaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoupdatableestimatoradaptor/tabularestimator-implementations)*