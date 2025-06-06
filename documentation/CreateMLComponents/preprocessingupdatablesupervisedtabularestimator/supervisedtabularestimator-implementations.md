# SupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](preprocessingupdatablesupervisedtabularestimator/appending(_:)-1utsg.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtabularestimator/appending(_:)-8vp2n.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtabularestimator/appending(_:)-gy7s.md)
  Composes this tabular supervised estimator with a tabular estimator.
- [func fitted(to: DataFrame, validateOn: DataFrame?) async throws -> Self.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](preprocessingupdatablesupervisedtabularestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatablesupervisedtabularestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator/supervisedtabularestimator-implementations)*