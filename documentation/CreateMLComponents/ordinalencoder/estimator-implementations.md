# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Structures
- [OrdinalEncoder.Transformer](ordinalencoder/transformer.md)
  A transformer that encodes a category as an integer.
### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](ordinalencoder/adaptedassupervised(annotationtype:)-43cy5.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](ordinalencoder/adaptedastemporal-45fik.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](ordinalencoder/appending(_:)-2pwgw.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](ordinalencoder/appending(_:)-5ntud.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](ordinalencoder/appending(_:)-67f9l.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](ordinalencoder/appending(_:)-9a1mi.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](ordinalencoder/appending(_:)-9luu.md)
  Composes this estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](ordinalencoder/appending(_:)-gbgx.md)
  Composes this estimator with a supervised temporal estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](ordinalencoder/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](ordinalencoder/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](ordinalencoder/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](ordinalencoder/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](ordinalencoder/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/ordinalencoder/estimator-implementations)*