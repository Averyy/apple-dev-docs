# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Structures
- [OneHotEncoder.Transformer](onehotencoder/transformer.md)
  A transformer that encodes a category as an array of integers.
### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](onehotencoder/adaptedassupervised(annotationtype:)-9si1o.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](onehotencoder/adaptedastemporal-3jzh6.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](onehotencoder/appending(_:)-11mvc.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](onehotencoder/appending(_:)-23h84.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](onehotencoder/appending(_:)-2c90d.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](onehotencoder/appending(_:)-4yjvh.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](onehotencoder/appending(_:)-7gvr3.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](onehotencoder/appending(_:)-9ujdo.md)
  Composes this estimator with a temporal transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](onehotencoder/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](onehotencoder/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](onehotencoder/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](onehotencoder/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](onehotencoder/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/onehotencoder/estimator-implementations)*