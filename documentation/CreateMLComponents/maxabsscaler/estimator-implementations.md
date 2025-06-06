# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Structures
- [MaxAbsScaler.Transformer](maxabsscaler/transformer.md)
  An transformer that scales the input values so that the maximum absolute value is 1.0.
### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](maxabsscaler/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](maxabsscaler/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](maxabsscaler/appending(_:)-1s16c.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](maxabsscaler/appending(_:)-37yde.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](maxabsscaler/appending(_:)-3ci1j.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](maxabsscaler/appending(_:)-4nl6j.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](maxabsscaler/appending(_:)-90wgn.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](maxabsscaler/appending(_:)-9b4bn.md)
  Composes this estimator with a supervised estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](maxabsscaler/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](maxabsscaler/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](maxabsscaler/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](maxabsscaler/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](maxabsscaler/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/maxabsscaler/estimator-implementations)*