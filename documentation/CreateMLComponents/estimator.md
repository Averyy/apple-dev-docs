# Estimator

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
protocol Estimator<Transformer>
```

## Topics

### Getting the properties
- [associatedtype Transformer : Transformer](estimator/transformer.md)
  The transformer type created by this estimator.
### Appending
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other>>
](estimator/appending(_:)-10qfn.md)
  Composes this estimator with a temporal transformer.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other.Transformer>>
](estimator/appending(_:)-1856y.md)
  Composes this estimator with another estimator.
- [func appending<Other>(Other) -> some SupervisedTemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>, Other.Annotation>
](estimator/appending(_:)-2xkyp.md)
  Composes this estimator with a supervised temporal estimator.
- [func appending<Other>(Other) -> some SupervisedEstimator<ComposedTransformer<Self.Transformer, Other.Transformer>, Other.Annotation>
](estimator/appending(_:)-atvs.md)
  Composes this estimator with a supervised estimator.
- [func appending<Other>(Other) -> some Estimator<ComposedTransformer<Self.Transformer, Other>>
](estimator/appending(_:)-u0ef.md)
  Composes this estimator with a transformer.
- [func appending<Other>(Other) -> some TemporalEstimator<ComposedTemporalTransformer<TransformerToTemporalAdaptor<Self.Transformer>, Other.Transformer>>
](estimator/appending(_:)-w1ek.md)
  Composes this estimator with a temporal estimator.
### Encoding and decoding
- [func encode(Self.Transformer, to: inout any EstimatorEncoder) throws](estimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> Self.Transformer](estimator/decode(from:).md)
  Decodes a previously fitted transformer.
### Reading and writing
- [func read(from: URL) throws -> Self.Transformer](estimator/read(from:).md)
  Reads the encoded transformer from a file.
- [func write(Self.Transformer, to: URL, overwrite: Bool) throws](estimator/write(_:to:overwrite:).md)
  Writes the encoded transformer to a file.
### Fitting and adapting
- [func adaptedAsSupervised<Annotation>(annotationType: Annotation.Type) -> EstimatorToSupervisedAdaptor<Self, Annotation>](estimator/adaptedassupervised(annotationtype:).md)
  Exposes this estimator as a supervised estimator.
- [func adaptedAsTemporal() -> EstimatorToTemporalAdaptor<Self>](estimator/adaptedastemporal.md)
  Exposes this estimator as a temporal estimator.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> Self.Transformer](estimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted<S>(to: S) async throws -> Self.Transformer](estimator/fitted(to:).md)

## Relationships

### Inherited By
- [UpdatableEstimator](updatableestimator.md)
### Conforming Types
- [CategoricalImputer](categoricalimputer.md)
- [MaxAbsScaler](maxabsscaler.md)
- [MinMaxScaler](minmaxscaler.md)
- [NormalizationScaler](normalizationscaler.md)
- [NumericImputer](numericimputer.md)
- [OneHotEncoder](onehotencoder.md)
- [OrdinalEncoder](ordinalencoder.md)
- [PreprocessingEstimator](preprocessingestimator.md)
- [PreprocessingUpdatableEstimator](preprocessingupdatableestimator.md)
- [RobustScaler](robustscaler.md)
- [StandardScaler](standardscaler.md)
- [TransformerToEstimatorAdaptor](transformertoestimatoradaptor.md)
- [TransformerToUpdatableEstimatorAdaptor](transformertoupdatableestimatoradaptor.md)

## See Also

- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.
- [protocol TemporalTransformer](temporaltransformer.md)
  A transformer that takes an asynchronous input sequence of temporal features and produces an asynchronous output  sequence.
- [protocol RandomTransformer](randomtransformer.md)
  A transformer that takes an input and a random number generator and produces a randomized output.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimator)*