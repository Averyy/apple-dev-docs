# TemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](estimatortotemporaladaptor/adaptedassupervised(annotationtype:).md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](estimatortotemporaladaptor/appending(_:)-12p4c.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](estimatortotemporaladaptor/appending(_:)-2497o.md)
  Composes this temporal estimator with a transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](estimatortotemporaladaptor/appending(_:)-6zvmc.md)
  Composes this temporal estimator with an estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](estimatortotemporaladaptor/appending(_:)-7kxqa.md)
  Composes this temporal estimator with a temporal transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](estimatortotemporaladaptor/appending(_:)-8vjki.md)
  Composes this temporal estimator with another temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](estimatortotemporaladaptor/appending(_:)-9cuep.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](estimatortotemporaladaptor/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](estimatortotemporaladaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](estimatortotemporaladaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortotemporaladaptor/temporalestimator-implementations)*