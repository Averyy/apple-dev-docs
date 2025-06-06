# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-2aouz.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-3nzss.md)
  Composes this supervised estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-5pmsl.md)
  Composes this supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-67zro.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-9xvcb.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedestimator/appending(_:)-wxtg.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](preprocessingupdatablesupervisedestimator/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](preprocessingupdatablesupervisedestimator/fitted(to:eventhandler:)-3dm84.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](preprocessingupdatablesupervisedestimator/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](preprocessingupdatablesupervisedestimator/fitted(to:validateon:eventhandler:)-98hf9.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](preprocessingupdatablesupervisedestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatablesupervisedestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedestimator/supervisedestimator-implementations)*