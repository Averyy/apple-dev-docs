# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](updatabletabularestimatortosupervisedadaptor/appending(_:)-5jfiq.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatabletabularestimatortosupervisedadaptor/appending(_:)-9dsfl.md)
  Composes this supervised tabular estimator with an updatable tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatabletabularestimatortosupervisedadaptor/appending(_:)-9w09l.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](updatabletabularestimatortosupervisedadaptor/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update(inout Self.Transformer, with: DataFrame) async throws](updatabletabularestimatortosupervisedadaptor/update(_:with:).md)
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](updatabletabularestimatortosupervisedadaptor/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimatortosupervisedadaptor/updatablesupervisedtabularestimator-implementations)*