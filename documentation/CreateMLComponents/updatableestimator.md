# UpdatableEstimator

**Framework**: Create ML Components  
**Kind**: protocol  
**Role**: Protocol

An estimator that can be incrementally updated.

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
protocol UpdatableEstimator<Transformer> : Estimator
```

## Topics

### Adapting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> UpdatableEstimatorToSupervisedAdaptor<Self, Annotation>](./updatableestimator/adaptedassupervised%28annotationtype%29.md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> UpdatableEstimatorToTemporalAdaptor<Self>](./updatableestimator/adaptedastemporal%28%29.md)
  Exposes this estimator as a temporal estimator.
### Appending
- [func appending(_:)](./updatableestimator/appending%28_%29.md)
  Composes this updatable estimator with another updatable estimator.
### Encoding and decoding
- [func encodeWithOptimizer(Self.Transformer, to: inout any EstimatorEncoder) throws](./updatableestimator/encodewithoptimizer%28_,to%29.md)
  Encodes the transformer and optimizer to an encoder.
- [func decodeWithOptimizer(from: inout any EstimatorDecoder) throws -> Self.Transformer](./updatableestimator/decodewithoptimizer%28from%29.md)
  Reads the encoded transformer and optimizer with a decoder.
### Transforming
- [func makeTransformer() -> Self.Transformer](./updatableestimator/maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./updatableestimator/update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence>(inout Self.Transformer, with: InputSequence) async throws](./updatableestimator/update%28_,with%29.md)

## Relationships

### Inherits From
- [Estimator](./estimator.md)
### Conforming Types
- [NumericImputer](./numericimputer.md)
- [OneHotEncoder](./onehotencoder.md)
- [OrdinalEncoder](./ordinalencoder.md)
- [PreprocessingUpdatableEstimator](./preprocessingupdatableestimator.md)
- [StandardScaler](./standardscaler.md)
- [TransformerToUpdatableEstimatorAdaptor](./transformertoupdatableestimatoradaptor.md)

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
- [protocol UpdatableSupervisedEstimator](./updatablesupervisedestimator.md)
  A supervised estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTemporalEstimator](./updatablesupervisedtemporalestimator.md)
  A supervised temporal estimator that can be incrementally updated.
- [protocol UpdatableSupervisedTabularEstimator](./updatablesupervisedtabularestimator.md)
  A supervised tabular estimator that can be incrementally updated.
- [protocol UpdatableTemporalEstimator](./updatabletemporalestimator.md)
  A temporal estimator that can be incrementally updated.
- [protocol UpdatableTabularEstimator](./updatabletabularestimator.md)
  A tabular estimator that can be incrementally updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/updatableestimator)*