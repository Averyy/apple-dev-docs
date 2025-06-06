# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](transformertoupdatableestimatoradaptor/adaptedassupervised(annotationtype:)-7ixb2.md)
  Exposes this estimator as a supervised estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](transformertoupdatableestimatoradaptor/appending(_:)-16v61.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](transformertoupdatableestimatoradaptor/appending(_:)-1xer0.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](transformertoupdatableestimatoradaptor/appending(_:)-2pw1u.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](transformertoupdatableestimatoradaptor/appending(_:)-5pn0q.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](transformertoupdatableestimatoradaptor/appending(_:)-9uaf0.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](transformertoupdatableestimatoradaptor/appending(_:)-lpfz.md)
  Composes this estimator with a supervised temporal estimator.
- [func fitted<S>(to: S) async throws -> Self.Transformer](transformertoupdatableestimatoradaptor/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](transformertoupdatableestimatoradaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](transformertoupdatableestimatoradaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/transformertoupdatableestimatoradaptor/estimator-implementations)*