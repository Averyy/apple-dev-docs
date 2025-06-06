# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-29go7.md)
  Composes this supervised estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-2eb29.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-30l0i.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-3i94f.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-46qiw.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](lineartimeseriesforecaster/appending(_:)-632rb.md)
  Composes this supervised estimator with a temporal transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> LinearTimeSeriesForecaster<Scalar>.Transformer](lineartimeseriesforecaster/decode(from:).md)
  Decodes a previously fitted model.
- [func encode(LinearTimeSeriesForecaster<Scalar>.Transformer, to: inout any EstimatorEncoder) throws](lineartimeseriesforecaster/encode(_:to:).md)
  Encodes a fitted model.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](lineartimeseriesforecaster/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](lineartimeseriesforecaster/fitted(to:eventhandler:)-9ayj2.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](lineartimeseriesforecaster/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](lineartimeseriesforecaster/fitted(to:validateon:eventhandler:)-6b8fs.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](lineartimeseriesforecaster/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](lineartimeseriesforecaster/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/lineartimeseriesforecaster/supervisedestimator-implementations)*