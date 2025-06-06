# TemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](temporaltransformertoupdatableestimatoradaptor/adaptedassupervised(annotationtype:)-397sv.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-1bv78.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-2wccr.md)
  Composes this temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-3r72v.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-5qbya.md)
  Composes this temporal estimator with another temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-62jtm.md)
  Composes this temporal estimator with an estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](temporaltransformertoupdatableestimatoradaptor/appending(_:)-8y9ux.md)
  Composes this temporal estimator with a temporal transformer.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](temporaltransformertoupdatableestimatoradaptor/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](temporaltransformertoupdatableestimatoradaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](temporaltransformertoupdatableestimatoradaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformertoupdatableestimatoradaptor/temporalestimator-implementations)*