# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-1vgho.md)
  Composes this supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-2b9c7.md)
  Composes this supervised estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-4tgti.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-6ywm3.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-7h6u9.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkclassifier/appending(_:)-95jkg.md)
  Composes this supervised estimator with another supervised estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkClassifierModel<Scalar, Label>](fullyconnectednetworkclassifier/decode(from:).md)
  Decodes the estimator.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkclassifier/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](fullyconnectednetworkclassifier/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](fullyconnectednetworkclassifier/fitted(to:eventhandler:)-9oepo.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](fullyconnectednetworkclassifier/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](fullyconnectednetworkclassifier/fitted(to:validateon:eventhandler:)-4zai9.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](fullyconnectednetworkclassifier/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](fullyconnectednetworkclassifier/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkclassifier/supervisedestimator-implementations)*