# SupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](supervisedestimatortotemporaladaptor/appending(_:)-1z96w.md)
  Composes this supervised temporal estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedestimatortotemporaladaptor/appending(_:)-2u938.md)
  Composes this supervised temporal estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](supervisedestimatortotemporaladaptor/appending(_:)-33c39.md)
  Composes this supervised temporal estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](supervisedestimatortotemporaladaptor/appending(_:)-5rvic.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedestimatortotemporaladaptor/appending(_:)-75rot.md)
  Composes this supervised temporal estimator with another supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](supervisedestimatortotemporaladaptor/appending(_:)-7nmw5.md)
  Composes this supervised temporal estimator with a transformer.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence) async throws -> Self.Transformer](supervisedestimatortotemporaladaptor/fitted(to:).md)
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation) async throws -> Self.Transformer](supervisedestimatortotemporaladaptor/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](supervisedestimatortotemporaladaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](supervisedestimatortotemporaladaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimatortotemporaladaptor/supervisedtemporalestimator-implementations)*