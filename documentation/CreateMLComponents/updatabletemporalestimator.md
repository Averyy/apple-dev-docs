# UpdatableTemporalEstimator

**Framework**: Create ML Components  
**Kind**: protocol

A temporal estimator that can be incrementally updated.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol UpdatableTemporalEstimator<Transformer> : TemporalEstimator
```

## Topics

### Appending
- [func appending(_:)](updatabletemporalestimator/appending(_:).md)
  Composes this updatable temporal estimator with an updatable supervised temporal estimator.
### Adapting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableTemporalEstimatorToSupervisedAdaptor<Self, Annotation>](updatabletemporalestimator/adaptedassupervised(annotationtype:).md)
  Exposes this temporal estimator as a supervised temporal estimator.
### Encoding and decoding
- [func encodeWithOptimizer(Self.Transformer, to: inout any EstimatorEncoder) throws](updatabletemporalestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Self.Transformer](updatabletemporalestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
### Transforming
- [func makeTransformer() -> Self.Transformer](updatabletemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](updatabletemporalestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](updatabletemporalestimator/update(_:with:).md)

## Relationships

### Inherits From
- [TemporalEstimator](temporalestimator.md)
### Conforming Types
- [PreprocessingUpdatableTemporalEstimator](preprocessingupdatabletemporalestimator.md)
- [TemporalTransformerToUpdatableEstimatorAdaptor](temporaltransformertoupdatableestimatoradaptor.md)
- [UpdatableEstimatorToTemporalAdaptor](updatableestimatortotemporaladaptor.md)

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
- [protocol UpdatableSupervisedTemporalEstimator](updatablesupervisedtemporalestimator.md)
  A supervised temporal estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTabularEstimator](updatablesupervisedtabularestimator.md)
  A supervised tabular estimator that can be incrementally updated.
- [protocol UpdatableTabularEstimator](updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletemporalestimator)*