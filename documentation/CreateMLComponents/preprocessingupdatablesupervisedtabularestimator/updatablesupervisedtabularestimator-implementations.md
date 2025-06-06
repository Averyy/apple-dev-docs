# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](preprocessingupdatablesupervisedtabularestimator/appending(_:)-4dglc.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtabularestimator/appending(_:)-4w0ec.md)
  Composes this supervised tabular estimator with an updatable tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](preprocessingupdatablesupervisedtabularestimator/appending(_:)-88nj7.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](preprocessingupdatablesupervisedtabularestimator/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update(inout Self.Transformer, with: DataFrame) async throws](preprocessingupdatablesupervisedtabularestimator/update(_:with:).md)
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](preprocessingupdatablesupervisedtabularestimator/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator/updatablesupervisedtabularestimator-implementations)*