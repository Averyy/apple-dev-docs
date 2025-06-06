# SupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](preprocessingsupervisedtemporalestimator/appending(_:)-1gpze.md)
  Composes this supervised temporal estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](preprocessingsupervisedtemporalestimator/appending(_:)-1rx9m.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingsupervisedtemporalestimator/appending(_:)-2u01s.md)
  Composes this supervised temporal estimator with another supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingsupervisedtemporalestimator/appending(_:)-3sj2j.md)
  Composes this supervised temporal estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](preprocessingsupervisedtemporalestimator/appending(_:)-4ead8.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](preprocessingsupervisedtemporalestimator/appending(_:)-7vkst.md)
  Composes this supervised temporal estimator with a supervised estimator.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence) async throws -> Self.Transformer](preprocessingsupervisedtemporalestimator/fitted(to:).md)
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation) async throws -> Self.Transformer](preprocessingsupervisedtemporalestimator/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](preprocessingsupervisedtemporalestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingsupervisedtemporalestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtemporalestimator/supervisedtemporalestimator-implementations)*