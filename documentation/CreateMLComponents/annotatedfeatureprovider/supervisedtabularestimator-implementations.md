# SupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](annotatedfeatureprovider/appending(_:)-7o9bo.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](annotatedfeatureprovider/appending(_:)-7ou4h.md)
  Composes this tabular supervised estimator with a tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](annotatedfeatureprovider/appending(_:)-j7oj.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func fitted(to: DataFrame, validateOn: DataFrame?) async throws -> Self.Transformer](annotatedfeatureprovider/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](annotatedfeatureprovider/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](annotatedfeatureprovider/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfeatureprovider/supervisedtabularestimator-implementations)*