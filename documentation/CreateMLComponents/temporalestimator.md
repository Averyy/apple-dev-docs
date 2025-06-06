# TemporalEstimator

**Framework**: Create ML Components  
**Kind**: protocol

An estimator that creates a transformer by fitting to a sequence of temporal features.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol TemporalEstimator<Transformer>
```

## Topics

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](temporalestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](temporalestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
### Appending
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other>>
](temporalestimator/appending(_:)-3ywtc.md)
  Composes this temporal estimator with a temporal transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](temporalestimator/appending(_:)-40b0.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>>
](temporalestimator/appending(_:)-43khh.md)
  Composes this temporal estimator with an estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other>>>
](temporalestimator/appending(_:)-5bepa.md)
  Composes this temporal estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<Self.Transformer, TransformerToTemporalAdaptor<Other.Transformer>>, Other.Annotation>
](temporalestimator/appending(_:)-90283.md)
  Composes this temporal estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<Self.Transformer, Other.Transformer>>
](temporalestimator/appending(_:)-933dy.md)
  Composes this temporal estimator with another temporal estimator.
### Adapting and fitting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> TemporalEstimatorToSupervisedAdaptor<Self, Annotation>](temporalestimator/adaptedassupervised(annotationtype:).md)
  Exposes this temporal estimator as a supervised temporal estimator.
- [func fitted<InputSequence>(to: InputSequence) async throws -> Self.Transformer](temporalestimator/fitted(to:).md)
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](temporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [associatedtype Transformer : TemporalTransformer](temporalestimator/transformer.md)
  The transformer type created by this estimator.
### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](temporalestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](temporalestimator/decode(from:).md)
  Decodes a previously fitted transformer.

## Relationships

### Inherited By
- [UpdatableTemporalEstimator](updatabletemporalestimator.md)
### Conforming Types
- [EstimatorToTemporalAdaptor](estimatortotemporaladaptor.md)
- [PreprocessingTemporalEstimator](preprocessingtemporalestimator.md)
- [PreprocessingUpdatableTemporalEstimator](preprocessingupdatabletemporalestimator.md)
- [TemporalTransformerToEstimatorAdaptor](temporaltransformertoestimatoradaptor.md)
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
- [protocol UpdatableTabularEstimator](updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporalestimator)*