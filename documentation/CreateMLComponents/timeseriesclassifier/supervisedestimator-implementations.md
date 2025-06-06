# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](timeseriesclassifier/appending(_:)-2vxib.md)
  Composes this supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-3a12t.md)
  Composes this supervised estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-5geo6.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-5oxs5.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](timeseriesclassifier/appending(_:)-88qrc.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](timeseriesclassifier/appending(_:)-8lf1c.md)
  Composes this supervised estimator with an estimator.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](timeseriesclassifier/decode(from:).md)
  Decodes a previously fitted decodable transformer.
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](timeseriesclassifier/encode(_:to:).md)
  Encodes a fitted encodable transformer.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](timeseriesclassifier/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](timeseriesclassifier/fitted(to:eventhandler:)-5ns43.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](timeseriesclassifier/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](timeseriesclassifier/fitted(to:validateon:eventhandler:)-94zlx.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](timeseriesclassifier/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](timeseriesclassifier/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesclassifier/supervisedestimator-implementations)*