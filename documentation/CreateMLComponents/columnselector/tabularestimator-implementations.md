# TabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> TabularEstimatorToSupervisedAdaptor<Self, Annotation>](columnselector/adaptedassupervised(annotationcolumnid:)-5jjef.md)
  Exposes this tabular estimator as a supervised tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](columnselector/appending(_:)-4g6ol.md)
  Compose this tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](columnselector/appending(_:)-6ase2.md)
  Composes this tabular estimator with a supervised tabular estimator.
- [func appending<Other>(Other) -> some TabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](columnselector/appending(_:)-70f9q.md)
  Compose this tabular estimator with another tabular estimator.
- [func fitted(to: DataFrame) async throws -> Self.Transformer](columnselector/fitted(to:)-3spu2.md)
- [func fitted(to: DataFrame) async throws -> Self.Transformer](columnselector/fitted(to:)-6xm37.md)
- [func read(from: URL) throws -> Self.Transformer](columnselector/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](columnselector/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/columnselector/tabularestimator-implementations)*