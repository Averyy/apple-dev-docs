# PreprocessingSupervisedEstimator

**Framework**: Create ML Components  
**Kind**: struct

A supervised estimator that composes a preprocessing transformer and a supervised estimator.

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
struct PreprocessingSupervisedEstimator<Preprocessor, Estimator> where Preprocessor : Transformer, Estimator : SupervisedEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating the estimator
- [init(Preprocessor, Estimator)](preprocessingsupervisedestimator/init(_:_:).md)
  Creates a composed supervised estimator from a preprocessing transformer and an estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingsupervisedestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingsupervisedestimator/preprocessor.md)
  The preprocessing transformer.
### Preprocessing and fitting
- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> AnySequence<AnnotatedFeature<Preprocessor.Output, PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Annotation>>](preprocessingsupervisedestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<S>(toPreprocessed: S, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [func fitted<InputSequence, Validation>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedestimator/fitted(to:validateon:eventhandler:).md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<Input, Validation>(toPreprocessed: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a composed transformer to a sequence of preprocessed features.
- [PreprocessingSupervisedEstimator.Annotation](preprocessingsupervisedestimator/annotation.md)
  The annotation type.
- [PreprocessingSupervisedEstimator.Input](preprocessingsupervisedestimator/input.md)
  The input type.
- [PreprocessingSupervisedEstimator.Intermediate](preprocessingsupervisedestimator/intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedEstimator.Output](preprocessingsupervisedestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SupervisedEstimator](supervisedestimator.md)

## See Also

- [struct PreprocessingEstimator](preprocessingestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingTemporalEstimator](preprocessingtemporalestimator.md)
  A temporal estimator that composes a preprocessing transformer and a temporal estimator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedestimator)*