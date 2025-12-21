# SupervisedTemporalEstimator

**Framework**: Create ML Components  
**Kind**: protocol

An estimator that creates a transformer by fitting to a sequence of annotated temporal features.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol SupervisedTemporalEstimator<Transformer, Annotation>
```

## Topics

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](supervisedtemporalestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](supervisedtemporalestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
- [associatedtype Annotation : Equatable, Sendable](supervisedtemporalestimator/annotation.md)
  The annotation type.
- [associatedtype Transformer : TemporalTransformer](supervisedtemporalestimator/transformer.md)
  The transformer type created by this estimator.
### Appending
- [func appending(_:)](supervisedtemporalestimator/appending(_:).md)
  Composes this supervised temporal estimator with another supervised temporal estimator.
### Fitting
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence) async throws -> Self.Transformer](supervisedtemporalestimator/fitted(to:).md)
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation) async throws -> Self.Transformer](supervisedtemporalestimator/fitted(to:validateon:).md)
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedtemporalestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [associatedtype Annotation : Equatable, Sendable](supervisedtemporalestimator/annotation.md)
  The annotation type.
- [associatedtype Transformer : TemporalTransformer](supervisedtemporalestimator/transformer.md)
  The transformer type created by this estimator.
### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](supervisedtemporalestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](supervisedtemporalestimator/decode(from:).md)
  Decodes a previously fitted transformer.

## Relationships

### Inherited By
- [UpdatableSupervisedTemporalEstimator](updatablesupervisedtemporalestimator.md)
### Conforming Types
- [PreprocessingSupervisedTemporalEstimator](preprocessingsupervisedtemporalestimator.md)
- [PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
- [SupervisedEstimatorToTemporalAdaptor](supervisedestimatortotemporaladaptor.md)
- [TemporalEstimatorToSupervisedAdaptor](temporalestimatortosupervisedadaptor.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedtemporalestimator)*