# SupervisedEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func adaptedAsTemporal() -> SupervisedEstimatorToTemporalAdaptor<Self>](logisticregressionclassifier/adaptedastemporal-2n9cf.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-1vw46.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-5bov8.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-6nsbl.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-7793l.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-9k7ee.md)
  Composes this supervised estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](logisticregressionclassifier/appending(_:)-i9r3.md)
  Composes this supervised estimator with a temporal estimator.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](logisticregressionclassifier/fitted(to:).md)
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](logisticregressionclassifier/fitted(to:eventhandler:)-9155b.md)
  Fits a transformer to an async sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](logisticregressionclassifier/fitted(to:validateon:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](logisticregressionclassifier/fitted(to:validateon:eventhandler:)-7hp54.md)
  Fits a transformer to an async sequence of examples while validating with a validation sequence.
- [func read(from: URL) throws -> Self.Transformer](logisticregressionclassifier/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](logisticregressionclassifier/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/supervisedestimator-implementations)*