# TemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](updatableestimatortotemporaladaptor/adaptedassupervised(annotationtype:)-3zq4c.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](updatableestimatortotemporaladaptor/appending(_:)-1m1rg.md)
  Composes this temporal estimator with another temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](updatableestimatortotemporaladaptor/appending(_:)-2iqx3.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](updatableestimatortotemporaladaptor/appending(_:)-2z8ro.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](updatableestimatortotemporaladaptor/appending(_:)-3pnei.md)
  Composes this temporal estimator with an estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](updatableestimatortotemporaladaptor/appending(_:)-9orv6.md)
  Composes this temporal estimator with a temporal transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](updatableestimatortotemporaladaptor/appending(_:)-x0dl.md)
  Composes this temporal estimator with a transformer.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](updatableestimatortotemporaladaptor/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](updatableestimatortotemporaladaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](updatableestimatortotemporaladaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimatortotemporaladaptor/temporalestimator-implementations)*