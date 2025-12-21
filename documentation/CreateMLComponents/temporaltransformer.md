# TemporalTransformer

**Framework**: Create ML Components  
**Kind**: protocol

A transformer that takes an asynchronous input sequence of temporal features and produces an asynchronous output  sequence.

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
protocol TemporalTransformer<Input, Output>
```

#### Overview

A temporal transformer, unlike a regular transformer, can accumulate multiple inputs before producing an output. For example, an audio transformer can accumulate audio buffers until the desired length is reached before producing an output.

## Topics

### Applying and adapting
- [func applied<S>(to: S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](temporaltransformer/applied(to:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func adaptedAsEstimator() -> TemporalTransformerToEstimatorAdaptor<Self>](temporaltransformer/adaptedasestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [func adaptedAsUpdatableEstimator() -> TemporalTransformerToUpdatableEstimatorAdaptor<Self>](temporaltransformer/adaptedasupdatableestimator.md)
  Exposes this temporal transformer as a trivial temporal estimator.
- [associatedtype Input](temporaltransformer/input.md)
  The input type.
- [associatedtype Output](temporaltransformer/output.md)
  The output type.
- [associatedtype OutputSequence : TemporalSequence](temporaltransformer/outputsequence.md)
  The output async sequence type.
### Appending
- [func appending(_:)](temporaltransformer/appending(_:).md)
  Composes this temporal transformer with another temporal transformer.
### Transforming and predicting
- [func callAsFunction<S>(S, eventHandler: EventHandler?) async throws -> Self.OutputSequence](temporaltransformer/callasfunction(_:eventhandler:).md)
  Performs the transformation on an input sequence.
- [func callAsFunction<S>(to: S, eventHandler: EventHandler?) async throws -> [Self.OutputSequence]](temporaltransformer/callasfunction(to:eventhandler:).md)
  Performs the transformation on a sequence of inputs.
- [func prediction<S, Label>(from: S) async throws -> Self.OutputSequence](temporaltransformer/prediction(from:).md)
  Performs a prediction on a single input.
### Exporting
- [func export(to: URL) throws](temporaltransformer/export(to:).md)
  Exports this temporal transformer as a CoreML model.
- [func export(to: URL, metadata: ModelMetadata) throws](temporaltransformer/export(to:metadata:).md)
  Exports this temporal transformer as a CoreML model with user-supplied metadata.

## Relationships

### Conforming Types
- [AudioFeaturePrint](audiofeatureprint.md)
- [ComposedTemporalTransformer](composedtemporaltransformer.md)
- [Downsampler](downsampler.md)
- [HumanBodyActionCounter](humanbodyactioncounter.md)
- [LinearTimeSeriesForecaster.Model](lineartimeseriesforecaster/model.md)
- [SlidingWindowTransformer](slidingwindowtransformer.md)
- [TemporalAdaptor](temporaladaptor.md)
- [TimeSeriesClassifier.Model](timeseriesclassifier/model.md)
- [TransformerToTemporalAdaptor](transformertotemporaladaptor.md)

## See Also

- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.
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
- [protocol UpdatableTabularEstimator](updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/temporaltransformer)*