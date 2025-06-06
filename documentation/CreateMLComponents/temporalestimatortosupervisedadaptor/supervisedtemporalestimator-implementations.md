# SupervisedTemporalEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](temporalestimatortosupervisedadaptor/appending(_:)-1s0wc.md)
  Composes this supervised temporal estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](temporalestimatortosupervisedadaptor/appending(_:)-7hv71.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](temporalestimatortosupervisedadaptor/appending(_:)-8tkzn.md)
  Composes this supervised temporal estimator with another supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](temporalestimatortosupervisedadaptor/appending(_:)-9kz3.md)
  Composes this supervised temporal estimator with a supervised estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](temporalestimatortosupervisedadaptor/appending(_:)-9rzar.md)
  Composes this supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](temporalestimatortosupervisedadaptor/appending(_:)-9wbts.md)
  Composes this supervised temporal estimator with an estimator.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence) async throws -> Self.Transformer](temporalestimatortosupervisedadaptor/fitted(to:).md)
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation) async throws -> Self.Transformer](temporalestimatortosupervisedadaptor/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](temporalestimatortosupervisedadaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](temporalestimatortosupervisedadaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimatortosupervisedadaptor/supervisedtemporalestimator-implementations)*