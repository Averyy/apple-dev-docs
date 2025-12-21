# UpdatableSupervisedTabularEstimator

**Framework**: Create ML Components  
**Kind**: protocol

A supervised tabular estimator that can be incrementally updated.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
protocol UpdatableSupervisedTabularEstimator<Transformer, Annotation> : SupervisedTabularEstimator
```

## Topics

### Appending
- [func appending(_:)](updatablesupervisedtabularestimator/appending(_:).md)
  Composes this supervised tabular estimator with another supervised tabular estimator.
### Encoding and decoding
- [func encodeWithOptimizer(Self.Transformer, to: inout any EstimatorEncoder) throws](updatablesupervisedtabularestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Self.Transformer](updatablesupervisedtabularestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
### Reading and writing
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](updatablesupervisedtabularestimator/readwithoptimizer(from:).md)
  Reads the encoded transformer and optimizer from a file.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](updatablesupervisedtabularestimator/writewithoptimizer(_:to:overwrite:).md)
  Writes the encoded transformer and optimizer to a file.
### Transforming
- [func makeTransformer() -> Self.Transformer](updatablesupervisedtabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout Self.Transformer, with: DataFrame) async throws](updatablesupervisedtabularestimator/update(_:with:).md)
- [func update(inout Self.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](updatablesupervisedtabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.

## Relationships

### Inherits From
- [SupervisedTabularEstimator](supervisedtabularestimator.md)
### Conforming Types
- [AnnotatedFeatureProvider](annotatedfeatureprovider.md)
- [BoostedTreeClassifier](boostedtreeclassifier.md)
- [BoostedTreeRegressor](boostedtreeregressor.md)
- [PreprocessingUpdatableSupervisedTabularEstimator](preprocessingupdatablesupervisedtabularestimator.md)
- [UpdatableTabularEstimatorToSupervisedAdaptor](updatabletabularestimatortosupervisedadaptor.md)

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
- [protocol UpdatableTemporalEstimator](updatabletemporalestimator.md)
  A temporal estimator that can be incrementally updated.
- [protocol UpdatableTabularEstimator](updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedtabularestimator)*