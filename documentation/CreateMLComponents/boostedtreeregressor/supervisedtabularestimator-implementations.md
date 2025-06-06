# SupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](boostedtreeregressor/appending(_:)-1nlv6.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](boostedtreeregressor/appending(_:)-4mup0.md)
  Composes this tabular supervised estimator with a tabular estimator.
- [func appending<Other>(Other) -> some SupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](boostedtreeregressor/appending(_:)-9g2fj.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func fitted(to: DataFrame, validateOn: DataFrame?) async throws -> Self.Transformer](boostedtreeregressor/fitted(to:validateon:).md)
- [func read(from: URL) throws -> Self.Transformer](boostedtreeregressor/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](boostedtreeregressor/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/boostedtreeregressor/supervisedtabularestimator-implementations)*