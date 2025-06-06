# SupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-1fpzz.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-2s903.md)
  Composes this supervised temporal estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-4zzey.md)
  Composes this supervised temporal estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-5kp4i.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-6b0pn.md)
  Composes this supervised temporal estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedestimatortotemporaladaptor/appending(_:)-j1sl.md)
  Composes this supervised temporal estimator with another supervised temporal estimator.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence) async throws -> Self.Transformer](updatablesupervisedestimatortotemporaladaptor/fitted(to:).md)
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation) async throws -> Self.Transformer](updatablesupervisedestimatortotemporaladaptor/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](updatablesupervisedestimatortotemporaladaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](updatablesupervisedestimatortotemporaladaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimatortotemporaladaptor/supervisedtemporalestimator-implementations)*