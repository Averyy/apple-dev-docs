# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Structures
- [StandardScaler.Transformer](standardscaler/transformer.md)
  A transformer that standardizes the input by removing the mean and scaling to unit variance.
### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](standardscaler/adaptedassupervised(annotationtype:)-32eyz.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](standardscaler/adaptedastemporal-60a5.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](standardscaler/appending(_:)-17q61.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](standardscaler/appending(_:)-1oekq.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](standardscaler/appending(_:)-2mtap.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](standardscaler/appending(_:)-2wazu.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](standardscaler/appending(_:)-4iq47.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](standardscaler/appending(_:)-9ls21.md)
  Composes this estimator with another estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](standardscaler/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](standardscaler/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](standardscaler/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](standardscaler/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](standardscaler/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/standardscaler/estimator-implementations)*