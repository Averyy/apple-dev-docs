# TabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](tabulartransformertoestimatoradaptor/adaptedassupervised(annotationcolumnid:).md)
  Exposes this tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](tabulartransformertoestimatoradaptor/appending(_:)-5e40l.md)
  Compose this tabular estimator with another tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](tabulartransformertoestimatoradaptor/appending(_:)-7pvwp.md)
  Composes this tabular estimator with a supervised tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](tabulartransformertoestimatoradaptor/appending(_:)-919eq.md)
  Compose this tabular estimator with a tabular transformer.
- [func fitted(to: DataFrame) async throws -> Self.Transformer](tabulartransformertoestimatoradaptor/fitted(to:)-3vdff.md)
- [func fitted(to: DataFrame) async throws -> Self.Transformer](tabulartransformertoestimatoradaptor/fitted(to:)-5lhyv.md)
- [func read(from: URL) throws -> Self.Transformer](tabulartransformertoestimatoradaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](tabulartransformertoestimatoradaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabulartransformertoestimatoradaptor/tabularestimator-implementations)*