# PreprocessingTemporalEstimator

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A temporal estimator that composes a preprocessing transformer and a temporal estimator.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
struct PreprocessingTemporalEstimator<Preprocessor, Estimator> where Preprocessor : TemporalTransformer, Estimator : TemporalEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](./preprocessingtemporalestimator/init%28_,_%29.md)
  Creates a composed temporal estimator from a preprocessing transformer and a temporal estimator.
### Getting the properties
- [var estimator: Estimator](./preprocessingtemporalestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](./preprocessingtemporalestimator/preprocessor.md)
  The preprocessing transformer.
### Preprocesing and fitting
- [func preprocessed<InputSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>]](./preprocessingtemporalestimator/preprocessed%28from,eventhandler%29.md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](./preprocessingtemporalestimator/fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](./preprocessingtemporalestimator/fitted%28topreprocessed,eventhandler%29.md)
  Fits a transformer to a sequence of preprocessed features.
- [PreprocessingTemporalEstimator.Input](./preprocessingtemporalestimator/input.md)
  The input type.
- [PreprocessingTemporalEstimator.Intermediate](./preprocessingtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTemporalEstimator.Output](./preprocessingtemporalestimator/output.md)
  The output type.
- [protocol Transformer](./transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TemporalEstimator](./temporalestimator.md)

## See Also

### Composition with preprocessing
- [struct PreprocessingEstimator](./preprocessingestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingSupervisedEstimator](./preprocessingsupervisedestimator.md)
  A supervised estimator that composes a preprocessing transformer and a supervised estimator.
- [struct PreprocessingSupervisedTemporalEstimator](./preprocessingsupervisedtemporalestimator.md)
  A supervised temporal estimator that composes a preprocessing transformer and a supervised temporal estimator.
- [struct PreprocessingUpdatableEstimator](./preprocessingupdatableestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.
- [struct PreprocessingUpdatableTemporalEstimator](./preprocessingupdatabletemporalestimator.md)
  An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator.
- [struct PreprocessingUpdatableSupervisedEstimator](./preprocessingupdatablesupervisedestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableSupervisedTemporalEstimator](./preprocessingupdatablesupervisedtemporalestimator.md)
  An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtemporalestimator)*