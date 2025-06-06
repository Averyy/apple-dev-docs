# PreprocessingEstimator

**Framework**: Create ML Components  
**Kind**: struct

An estimator that composes a preprocessing transformer and an estimator.

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
struct PreprocessingEstimator<Preprocessor, Estimator> where Preprocessor : Transformer, Estimator : Estimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingestimator/init(_:_:).md)
  Creates a composed estimator from a preprocessing transformer and an estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encode(PreprocessingEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer](preprocessingestimator/decode(from:).md)
  Decodes a previously fitted transformer.
### Preprocesing and fitting
- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> [Preprocessor.Output]](preprocessingestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer](preprocessingestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<S>(toPreprocessed: S, eventHandler: EventHandler?) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer](preprocessingestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [PreprocessingEstimator.Input](preprocessingestimator/input.md)
  The input type.
- [PreprocessingEstimator.Intermediate](preprocessingestimator/intermediate.md)
  The intermediate type.
- [PreprocessingEstimator.Output](preprocessingestimator/output.md)
  The output type.
- [PreprocessingEstimator.Transformer](preprocessingestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [Estimator Implementations](preprocessingestimator/estimator-implementations.md)

## Relationships

### Conforms To
- [Estimator](estimator.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct PreprocessingTemporalEstimator](preprocessingtemporalestimator.md)
  A temporal estimator that composes a preprocessing transformer and a temporal estimator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingestimator)*