# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> SupervisedEstimatorToTemporalAdaptor<Self>](estimatortosupervisedadaptor/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](estimatortosupervisedadaptor/appending(_:)-465cu.md)
  Composes this supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](estimatortosupervisedadaptor/appending(_:)-4lm0x.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](estimatortosupervisedadaptor/appending(_:)-5zhlu.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](estimatortosupervisedadaptor/appending(_:)-662r2.md)
  Composes this supervised estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](estimatortosupervisedadaptor/appending(_:)-71b2f.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](estimatortosupervisedadaptor/appending(_:)-bxl4.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](estimatortosupervisedadaptor/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](estimatortosupervisedadaptor/fitted(to:eventhandler:)-164a9.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](estimatortosupervisedadaptor/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](estimatortosupervisedadaptor/fitted(to:validateon:eventhandler:)-4jmz7.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](estimatortosupervisedadaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](estimatortosupervisedadaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatortosupervisedadaptor/supervisedestimator-implementations)*