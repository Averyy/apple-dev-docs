# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-1prt1.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-2fvpg.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-4qgeg.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-5eed2.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-5mr1w.md)
  Composes this supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](fullyconnectednetworkmultilabelclassifier/appending(_:)-89ztt.md)
  Composes this supervised estimator with a temporal estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>](fullyconnectednetworkmultilabelclassifier/decode(from:).md)
  Decodes the estimator.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](fullyconnectednetworkmultilabelclassifier/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](fullyconnectednetworkmultilabelclassifier/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](fullyconnectednetworkmultilabelclassifier/fitted(to:eventhandler:)-w5i4.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](fullyconnectednetworkmultilabelclassifier/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](fullyconnectednetworkmultilabelclassifier/fitted(to:validateon:eventhandler:)-8pgge.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](fullyconnectednetworkmultilabelclassifier/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](fullyconnectednetworkmultilabelclassifier/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifier/supervisedestimator-implementations)*