# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](preprocessingupdatableestimator/adaptedassupervised(annotationtype:)-5auoj.md)
  Exposes this estimator as a supervised estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](preprocessingupdatableestimator/appending(_:)-3fhgg.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](preprocessingupdatableestimator/appending(_:)-3k09n.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](preprocessingupdatableestimator/appending(_:)-44lbc.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](preprocessingupdatableestimator/appending(_:)-497ju.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](preprocessingupdatableestimator/appending(_:)-5bql9.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](preprocessingupdatableestimator/appending(_:)-8enp4.md)
  Composes this estimator with a supervised estimator.
- [func fitted<S>(to: S) async throws -> Self.Transformer](preprocessingupdatableestimator/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](preprocessingupdatableestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatableestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatableestimator/estimator-implementations)*