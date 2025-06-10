# PreprocessingTemporalEstimator

**Framework**: Create ML Components  
**Kind**: struct

A temporal estimator that composes a preprocessing transformer and a temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct PreprocessingTemporalEstimator<Preprocessor, Estimator> where Preprocessor : TemporalTransformer, Estimator : TemporalEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingtemporalestimator/init(_:_:).md)
  Creates a composed temporal estimator from a preprocessing transformer and a temporal estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingtemporalestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingtemporalestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encode(PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingtemporalestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/decode(from:).md)
  Decodes a previously fitted transformer.
### Preprocesing and fitting
- [func preprocessed<InputSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>]](preprocessingtemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingtemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [PreprocessingTemporalEstimator.Input](preprocessingtemporalestimator/input.md)
  The input type.
- [PreprocessingTemporalEstimator.Intermediate](preprocessingtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTemporalEstimator.Output](preprocessingtemporalestimator/output.md)
  The output type.
- [PreprocessingTemporalEstimator.Transformer](preprocessingtemporalestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [TemporalEstimator Implementations](preprocessingtemporalestimator/temporalestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalEstimator](temporalestimator.md)

## See Also

- [struct PreprocessingEstimator](preprocessingestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingSupervisedEstimator](preprocessingsupervisedestimator.md)
  A supervised estimator that composes a preprocessing transformer and a supervised estimator.
- [struct PreprocessingSupervisedTemporalEstimator](preprocessingsupervisedtemporalestimator.md)
  A supervised temporal estimator that composes a preprocessing transformer and a supervised temporal estimator.
- [struct PreprocessingUpdatableEstimator](preprocessingupdatableestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.
- [struct PreprocessingUpdatableTemporalEstimator](preprocessingupdatabletemporalestimator.md)
  An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator.
- [struct PreprocessingUpdatableSupervisedEstimator](preprocessingupdatablesupervisedestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
  An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtemporalestimator)*