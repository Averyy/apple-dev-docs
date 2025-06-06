# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](annotatedfeatureprovider/appending(_:)-1vixp.md)
  Composes this supervised tabular estimator with an updatable tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](annotatedfeatureprovider/appending(_:)-42te1.md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>, Self.Annotation>
](annotatedfeatureprovider/appending(_:)-8b05x.md)
  Composes this supervised tabular estimator with a tabular transformer.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer](annotatedfeatureprovider/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer, to: inout any EstimatorEncoder) throws](annotatedfeatureprovider/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer](annotatedfeatureprovider/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](annotatedfeatureprovider/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func update(inout Self.Transformer, with: DataFrame) async throws](annotatedfeatureprovider/update(_:with:).md)
- [func update(inout AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](annotatedfeatureprovider/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](annotatedfeatureprovider/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfeatureprovider/updatablesupervisedtabularestimator-implementations)*