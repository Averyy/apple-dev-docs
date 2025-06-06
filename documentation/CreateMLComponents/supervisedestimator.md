# SupervisedEstimator

**Framework**: Create ML Components  
**Kind**: protocol

An estimator that creates a transformer by fitting to a data set.

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
protocol SupervisedEstimator<Transformer, Annotation>
```

## Topics

### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](supervisedestimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](supervisedestimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
- [associatedtype Annotation : Equatable](supervisedestimator/annotation.md)
  The annotation type.
- [associatedtype Transformer : Transformer](supervisedestimator/transformer.md)
  The transformer type created by this estimator.
### Appending
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](supervisedestimator/appending(_:)-2436m.md)
  Composes this supervised estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedestimator/appending(_:)-36sou.md)
  Composes this supervised estimator with another supervised estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Self.Annotation>
](supervisedestimator/appending(_:)-48wwd.md)
  Composes this supervised estimator with an estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other>, Self.Annotation>
](supervisedestimator/appending(_:)-629ia.md)
  Composes this supervised estimator with a transformer.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Self.Annotation>
](supervisedestimator/appending(_:)-8mm57.md)
  Composes this supervised estimator with a temporal estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>, Self.Annotation>
](supervisedestimator/appending(_:)-m18k.md)
  Composes this supervised estimator with a temporal transformer.
### Adapting and fitting
- [func adaptedAsTemporal() -> SupervisedEstimatorToTemporalAdaptor<Self>](supervisedestimator/adaptedastemporal.md)
  Exposes this supervised estimator as a temporal supervised estimator.
- [func fitted<Input>(to: Input, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<Input, Validation>(to: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> Self.Transformer](supervisedestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func fitted<Input>(to: Input) async throws -> Self.Transformer](supervisedestimator/fitted(to:).md)
- [func fitted<Input, Validation>(to: Input, validateOn: Validation) async throws -> Self.Transformer](supervisedestimator/fitted(to:validateon:).md)
### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](supervisedestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](supervisedestimator/decode(from:).md)
  Decodes a previously fitted transformer.

## Relationships

### Inherited By
- [UpdatableSupervisedEstimator](updatablesupervisedestimator.md)
### Conforming Types
- [EstimatorToSupervisedAdaptor](estimatortosupervisedadaptor.md)
- [FullyConnectedNetworkClassifier](fullyconnectednetworkclassifier.md)
- [FullyConnectedNetworkMultiLabelClassifier](fullyconnectednetworkmultilabelclassifier.md)
- [FullyConnectedNetworkRegressor](fullyconnectednetworkregressor.md)
- [LinearRegressor](linearregressor.md)
- [LinearTimeSeriesForecaster](lineartimeseriesforecaster.md)
- [LogisticRegressionClassifier](logisticregressionclassifier.md)
- [MultivariateLinearRegressor](multivariatelinearregressor.md)
- [PreprocessingSupervisedEstimator](preprocessingsupervisedestimator.md)
- [PreprocessingUpdatableSupervisedEstimator](preprocessingupdatablesupervisedestimator.md)
- [TimeSeriesClassifier](timeseriesclassifier.md)
- [UpdatableEstimatorToSupervisedAdaptor](updatableestimatortosupervisedadaptor.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/supervisedestimator)*