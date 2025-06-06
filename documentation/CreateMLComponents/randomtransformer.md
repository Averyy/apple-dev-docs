# RandomTransformer

**Framework**: Create ML Components  
**Kind**: protocol

A transformer that takes an input and a random number generator and produces a randomized output.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
protocol RandomTransformer<Input, Output>
```

## Topics

### Performing the transformation
- [func applied(to: Self.Input, generator: inout some RandomNumberGenerator, eventHandler: EventHandler?) async throws -> Self.Output](randomtransformer/applied(to:generator:eventhandler:).md)
  Performs the random transformation on a single input.
- [associatedtype Input](randomtransformer/input.md)
  The input type.
- [associatedtype Output](randomtransformer/output.md)
  The output type.

## Relationships

### Conforming Types
- [ApplyEachRandomly](applyeachrandomly.md)
- [ApplyRandomly](applyrandomly.md)
- [ChooseRandomly](chooserandomly.md)
- [RandomImageCropper](randomimagecropper.md)
- [ShuffleRandomly](shufflerandomly.md)
- [UniformRandomFloatingPointParameter](uniformrandomfloatingpointparameter.md)
- [UniformRandomIntegerParameter](uniformrandomintegerparameter.md)

## See Also

- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.
- [protocol TemporalTransformer](temporaltransformer.md)
  A transformer that takes an asynchronous input sequence of temporal features and produces an asynchronous output  sequence.
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
- [protocol UpdatableTabularEstimator](updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/randomtransformer)*