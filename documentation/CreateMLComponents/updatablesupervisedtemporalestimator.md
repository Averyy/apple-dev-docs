# UpdatableSupervisedTemporalEstimator

**Framework**: Create ML Components  
**Kind**: protocol

A supervised temporal estimator that can be incrementally updated.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol UpdatableSupervisedTemporalEstimator<Transformer, Annotation> : SupervisedTemporalEstimator
```

## Topics

### Appending
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-1sjwg.md)
  Composes this updatable supervised temporal estimator with another updatable supervised temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-30xpc.md)
  Composes this updatable supervised temporal estimator with an updatable temporal estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-3k3xn.md)
  Composes this updatable supervised temporal estimator with a transformer.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-4xdv5.md)
  Composes this updatable supervised temporal estimator with an updatable estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-7orql.md)
  Composes this updatable supervised temporal estimator with an updatable supervised estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>, Self.Annotation>
](updatablesupervisedtemporalestimator/appending(_:)-8wg63.md)
  Composes this updatable supervised temporal estimator with a transformer.
### Encoding and decoding
- [func encodeWithOptimizer(Self.Transformer, to: inout any EstimatorEncoder) throws](updatablesupervisedtemporalestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Self.Transformer](updatablesupervisedtemporalestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
### Reading and writing
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](updatablesupervisedtemporalestimator/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](updatablesupervisedtemporalestimator/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.
### Transforming
- [func makeTransformer() -> Self.Transformer](updatablesupervisedtemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout Self.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatablesupervisedtemporalestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, FeatureSequence>(inout Self.Transformer, with: InputSequence) async throws](updatablesupervisedtemporalestimator/update(_:with:).md)

## Relationships

### Inherits From
- [SupervisedTemporalEstimator](supervisedtemporalestimator.md)
### Conforming Types
- [PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
- [UpdatableSupervisedEstimatorToTemporalAdaptor](updatablesupervisedestimatortotemporaladaptor.md)
- [UpdatableTemporalEstimatorToSupervisedAdaptor](updatabletemporalestimatortosupervisedadaptor.md)

## See Also

- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.
- [protocol TemporalTransformer](temporaltransformer.md)
  A transformer that takes an asynchronous input sequence of temporal features and produces an asynchronous output  sequence.
- [protocol RandomTransformer](randomtransformer.md)
  A transformer that takes an input and a random number generator and produces a randomized output.
- [protocol Estimator](estimator.md)
  An estimator that creates a transformer by fitting to a data set.
- [protocol TemporalEstimator](temporalestimator.md)
  An estimator that creates a transformer by fitting to a sequence of temporal features.
- [protocol SupervisedEstimator](supervisedestimator.md)
  An estimator that creates a transformer by fitting to a data set.
- [protocol SupervisedTemporalEstimator](supervisedtemporalestimator.md)
  An estimator that creates a transformer by fitting to a sequence of annotated temporal features.
- [protocol UpdatableEstimator](updatableestimator.md)
  An estimator that can be incrementally updated.
- [protocol UpdatableSupervisedEstimator](updatablesupervisedestimator.md)
  A supervised estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTabularEstimator](updatablesupervisedtabularestimator.md)
  A supervised tabular estimator that can be incrementally updated.
- [protocol UpdatableTemporalEstimator](updatabletemporalestimator.md)
  A temporal estimator that can be incrementally updated.
- [protocol UpdatableTabularEstimator](updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtemporalestimator)*