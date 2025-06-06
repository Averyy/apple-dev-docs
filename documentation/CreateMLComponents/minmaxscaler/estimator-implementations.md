# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Structures
- [MinMaxScaler.Transformer](minmaxscaler/transformer.md)
  A transformer that scales the input values so that they all lie in a closed range.
### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](minmaxscaler/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](minmaxscaler/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](minmaxscaler/appending(_:)-1thwk.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](minmaxscaler/appending(_:)-2d4yy.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](minmaxscaler/appending(_:)-4vfyh.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](minmaxscaler/appending(_:)-c32h.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](minmaxscaler/appending(_:)-ryv0.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](minmaxscaler/appending(_:)-sje2.md)
  Composes this estimator with another estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](minmaxscaler/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](minmaxscaler/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](minmaxscaler/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](minmaxscaler/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](minmaxscaler/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/minmaxscaler/estimator-implementations)*