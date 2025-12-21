# UpdatableSupervisedTabularEstimator Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer](annotatedfeatureprovider/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
- [func encodeWithOptimizer(AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer, to: inout any EstimatorEncoder) throws](annotatedfeatureprovider/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func makeTransformer() -> AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer](annotatedfeatureprovider/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout AnnotatedFeatureProvider<Base, UnwrappedInput>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](annotatedfeatureprovider/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/annotatedfeatureprovider/updatablesupervisedtabularestimator-implementations)*