# Estimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](numericimputer/adaptedassupervised(annotationtype:)-8x9qv.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](numericimputer/adaptedastemporal-3nxt6.md)
  Exposes this estimator as a temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](numericimputer/appending(_:)-1igfs.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](numericimputer/appending(_:)-2zs2o.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](numericimputer/appending(_:)-3ecjt.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](numericimputer/appending(_:)-49biv.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](numericimputer/appending(_:)-56c2b.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](numericimputer/appending(_:)-5gehh.md)
  Composes this estimator with a temporal estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](numericimputer/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](numericimputer/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<S>(to: S) async throws -> Self.Transformer](numericimputer/fitted(to:).md)
- [func read(from: URL) throws -> Self.Transformer](numericimputer/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](numericimputer/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/numericimputer/estimator-implementations)*