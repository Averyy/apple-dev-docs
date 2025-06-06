# SupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-1dnbe.md)
  Composes this supervised temporal estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-1lkhn.md)
  Composes this supervised temporal estimator with another supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-50uag.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-54aj4.md)
  Composes this supervised temporal estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-8p4a9.md)
  Composes this supervised temporal estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](preprocessingupdatablesupervisedtemporalestimator/appending(_:)-wymt.md)
  Composes this supervised temporal estimator with a transformer.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence) async throws -> Self.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(to:).md)
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation) async throws -> Self.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](preprocessingupdatablesupervisedtemporalestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatablesupervisedtemporalestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator/supervisedtemporalestimator-implementations)*