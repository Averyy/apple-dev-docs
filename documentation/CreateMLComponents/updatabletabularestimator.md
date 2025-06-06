# UpdatableTabularEstimator

**Framework**: Create ML Components  
**Kind**: protocol

A tabular estimator that can be incrementally updated.

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
protocol UpdatableTabularEstimator<Transformer> : TabularEstimator
```

## Topics

### Appending
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other>>
](updatabletabularestimator/appending(_:)-3sl33.md)
  Composes this updatable tabular estimator with a tabular transformer.
- [func appending<Other>(Other) -> some UpdatableTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>>
](updatabletabularestimator/appending(_:)-700m8.md)
  Composes this updatable tabular estimator with another updatable tabular estimator.
- [func appending<Other>(Other) -> some UpdatableSupervisedTabularEstimator<ComposedTabularTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](updatabletabularestimator/appending(_:)-9shn1.md)
  Composes this updatable tabular estimator with an updatable supervised tabular estimator.
### Adapting
- [func adaptedAsSupervised<Annotation>(annotationColumnID: ColumnID<Annotation>) -> UpdatableTabularEstimatorToSupervisedAdaptor<Self, Annotation>](updatabletabularestimator/adaptedassupervised(annotationcolumnid:).md)
  Exposes this updatable tabular estimator as a supervised tabular estimator.
### Encoding and decoding
- [func encodeWithOptimizer(Self.Transformer, to: inout any EstimatorEncoder) throws](updatabletabularestimator/encodewithoptimizer(_:to:).md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Self.Transformer](updatabletabularestimator/decodewithoptimizer(from:).md)
  Reads the encoded transformer and optimizer with a decoder.
### Transforming
- [func makeTransformer() -> Self.Transformer](updatabletabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update(inout Self.Transformer, with: DataFrame) async throws](updatabletabularestimator/update(_:with:).md)
- [func update(inout Self.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](updatabletabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.

## Relationships

### Inherits From
- [TabularEstimator](tabularestimator.md)
### Conforming Types
- [ColumnSelector](columnselector.md)
- [PreprocessingUpdatableTabularEstimator](preprocessingupdatabletabularestimator.md)
- [TabularTransformerToUpdatableEstimatorAdaptor](tabulartransformertoupdatableestimatoradaptor.md)

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
- [protocol UpdatableTemporalEstimator](updatabletemporalestimator.md)
  A temporal estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatabletabularestimator)*