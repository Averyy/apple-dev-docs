# TemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](preprocessingupdatabletemporalestimator/adaptedassupervised(annotationtype:)-1o0lg.md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](preprocessingupdatabletemporalestimator/appending(_:)-32zhp.md)
  Composes this temporal estimator with an estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](preprocessingupdatabletemporalestimator/appending(_:)-3fqte.md)
  Composes this temporal estimator with another temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](preprocessingupdatabletemporalestimator/appending(_:)-89idv.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](preprocessingupdatabletemporalestimator/appending(_:)-8nxk2.md)
  Composes this temporal estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](preprocessingupdatabletemporalestimator/appending(_:)-90zzd.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](preprocessingupdatabletemporalestimator/appending(_:)-9n1za.md)
  Composes this temporal estimator with a transformer.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](preprocessingupdatabletemporalestimator/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](preprocessingupdatabletemporalestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatabletemporalestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletemporalestimator/temporalestimator-implementations)*