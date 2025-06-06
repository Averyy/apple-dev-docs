# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-1bamt.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-1kj90.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-2dxz4.md)
  Composes this supervised estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-329nr.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-3x8b3.md)
  Composes this supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkregressor/appending(_:)-54qsd.md)
  Composes this supervised estimator with an estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkRegressorModel<Scalar>](fullyconnectednetworkregressor/decode(from:).md)
  Decodes the estimator.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkregressor/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](fullyconnectednetworkregressor/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](fullyconnectednetworkregressor/fitted(to:eventhandler:)-29zu2.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](fullyconnectednetworkregressor/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](fullyconnectednetworkregressor/fitted(to:validateon:eventhandler:)-9w8y8.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](fullyconnectednetworkregressor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](fullyconnectednetworkregressor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkregressor/supervisedestimator-implementations)*