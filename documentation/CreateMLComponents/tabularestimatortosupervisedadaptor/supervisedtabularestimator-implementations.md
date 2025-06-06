# SupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](tabularestimatortosupervisedadaptor/appending(_:)-2soba.md)
  Composes this tabular supervised estimator with a tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](tabularestimatortosupervisedadaptor/appending(_:)-5gkwi.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](tabularestimatortosupervisedadaptor/appending(_:)-68c52.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func fitted(to: DataFrame, validateOn: DataFrame?) async throws -> Self.Transformer](tabularestimatortosupervisedadaptor/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](tabularestimatortosupervisedadaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](tabularestimatortosupervisedadaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/tabularestimatortosupervisedadaptor/supervisedtabularestimator-implementations)*