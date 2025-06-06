# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Structures
- [NormalizationScaler.Transformer](normalizationscaler/transformer.md)
  A transformer that scales the input using a normalization strategy.
### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](normalizationscaler/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](normalizationscaler/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](normalizationscaler/appending(_:)-23yek.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](normalizationscaler/appending(_:)-2q7jo.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](normalizationscaler/appending(_:)-30m7s.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](normalizationscaler/appending(_:)-3ktp4.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](normalizationscaler/appending(_:)-6ch6e.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](normalizationscaler/appending(_:)-6tstv.md)
  Composes this estimator with another estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](normalizationscaler/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](normalizationscaler/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](normalizationscaler/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](normalizationscaler/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](normalizationscaler/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/normalizationscaler/estimator-implementations)*