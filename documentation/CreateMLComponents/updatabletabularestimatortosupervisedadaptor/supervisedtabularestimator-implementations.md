# SupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatabletabularestimatortosupervisedadaptor/appending(_:)-4ci9o.md)
  Composes this tabular supervised estimator with a tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatabletabularestimatortosupervisedadaptor/appending(_:)-77w1i.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](updatabletabularestimatortosupervisedadaptor/appending(_:)-88zu1.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func fitted(to: DataFrame, validateOn: DataFrame?) async throws -> Self.Transformer](updatabletabularestimatortosupervisedadaptor/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](updatabletabularestimatortosupervisedadaptor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](updatabletabularestimatortosupervisedadaptor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimatortosupervisedadaptor/supervisedtabularestimator-implementations)*