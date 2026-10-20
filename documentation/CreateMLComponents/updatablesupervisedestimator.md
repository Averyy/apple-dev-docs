# UpdatableSupervisedEstimator

**Framework**: Create ML Components  
**Kind**: protocol  
**Role**: Protocol

A supervised estimator that can be incrementally updated.

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
protocol UpdatableSupervisedEstimator<Transformer, Annotation> : SupervisedEstimator
```

## Topics

### Appending
- [func appending(_:)](./updatablesupervisedestimator/appending%28_%29.md)
  Composes this updatable estimator with an updatable estimator.
### Adapting
- [func adaptedAsTemporal() -> UpdatableSupervisedEstimatorToTemporalAdaptor<Self>](./updatablesupervisedestimator/adaptedastemporal%28%29.md)
  Exposes this supervised estimator as a temporal supervised estimator.
### Encoding and decoding
- [func encodeWithOptimizer(Self.Transformer, to: inout any EstimatorEncoder) throws](./updatablesupervisedestimator/encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Self.Transformer](./updatablesupervisedestimator/decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer with a decoder.
### Reading and writing
- [func readWithOptimizer(from: URL) throws -> Self.Transformer](./updatablesupervisedestimator/readwithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer from a file.
- [func writeWithOptimizer(Self.Transformer, to: URL, overwrite: Bool) throws](./updatablesupervisedestimator/writewithoptimizer%28_,to,overwrite%29.md)
  Writes the encoded transformer and optimizer to a file.
### Transforming
- [func makeTransformer() -> Self.Transformer](./updatablesupervisedestimator/maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./updatablesupervisedestimator/update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](./updatablesupervisedestimator/update%28_,with%29.md)

## Relationships

### Inherits From
- [SupervisedEstimator](./supervisedestimator.md)
### Conforming Types
- [FullyConnectedNetworkClassifier](./fullyconnectednetworkclassifier.md)
- [FullyConnectedNetworkMultiLabelClassifier](./fullyconnectednetworkmultilabelclassifier.md)
- [FullyConnectedNetworkRegressor](./fullyconnectednetworkregressor.md)
- [LinearRegressor](./linearregressor.md)
- [LinearTimeSeriesForecaster](./lineartimeseriesforecaster.md)
- [LogisticRegressionClassifier](./logisticregressionclassifier.md)
- [MultivariateLinearRegressor](./multivariatelinearregressor.md)
- [PreprocessingUpdatableSupervisedEstimator](./preprocessingupdatablesupervisedestimator.md)
- [TimeSeriesClassifier](./timeseriesclassifier.md)
- [UpdatableEstimatorToSupervisedAdaptor](./updatableestimatortosupervisedadaptor.md)

## See Also

### Protocols
- [protocol Transformer](./transformer.md)
  A transformer that takes an input and produces an output.
- [protocol TemporalTransformer](./temporaltransformer.md)
  A transformer that takes an asynchronous input sequence of temporal features and produces an asynchronous output  sequence.
- [protocol RandomTransformer](./randomtransformer.md)
  A transformer that takes an input and a random number generator and produces a randomized output.
- [protocol Estimator](./estimator.md)
  An estimator that creates a transformer by fitting to a data set.
- [protocol TemporalEstimator](./temporalestimator.md)
  An estimator that creates a transformer by fitting to a sequence of temporal features.
- [protocol SupervisedEstimator](./supervisedestimator.md)
  An estimator that creates a transformer by fitting to a data set.
- [protocol SupervisedTemporalEstimator](./supervisedtemporalestimator.md)
  An estimator that creates a transformer by fitting to a sequence of annotated temporal features.
- [protocol UpdatableEstimator](./updatableestimator.md)
  An estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTemporalEstimator](./updatablesupervisedtemporalestimator.md)
  A supervised temporal estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTabularEstimator](./updatablesupervisedtabularestimator.md)
  A supervised tabular estimator that can be incrementally updated.
- [protocol UpdatableTemporalEstimator](./updatabletemporalestimator.md)
  A temporal estimator that can be incrementally updated.
- [protocol UpdatableTabularEstimator](./updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatablesupervisedestimator)*