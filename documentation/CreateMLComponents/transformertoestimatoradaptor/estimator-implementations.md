# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](transformertoestimatoradaptor/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](transformertoestimatoradaptor/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](transformertoestimatoradaptor/appending(_:)-1252y.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](transformertoestimatoradaptor/appending(_:)-1npz4.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](transformertoestimatoradaptor/appending(_:)-4t1j.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](transformertoestimatoradaptor/appending(_:)-8woqg.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](transformertoestimatoradaptor/appending(_:)-9y6ri.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](transformertoestimatoradaptor/appending(_:)-b9f7.md)
  Composes this estimator with a transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](transformertoestimatoradaptor/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](transformertoestimatoradaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](transformertoestimatoradaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoestimatoradaptor/estimator-implementations)*