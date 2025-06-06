# PreprocessingSupervisedTemporalEstimator

**Framework**: Create ML Components  
**Kind**: struct

A supervised temporal estimator that composes a preprocessing transformer and a supervised temporal estimator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator> where Preprocessor : TemporalTransformer, Estimator : SupervisedTemporalEstimator, Preprocessor.Output == Estimator.Transformer.Input
```

## Topics

### Creating an estimator
- [init(Preprocessor, Estimator)](preprocessingsupervisedtemporalestimator/init(_:_:).md)
  Creates a composed supervised temporal estimator from a preprocessing transformer and a supervised temporal estimator.
### Getting the properties
- [var estimator: Estimator](preprocessingsupervisedtemporalestimator/estimator.md)
  The estimator.
- [var preprocessor: Preprocessor](preprocessingsupervisedtemporalestimator/preprocessor.md)
  The preprocessing transformer.
### Encoding and decoding
- [func encode(PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, to: inout any EstimatorEncoder) throws](preprocessingsupervisedtemporalestimator/encode(_:to:).md)
  Encodes a fitted transformer.
- [func decode(from: inout any EstimatorDecoder) throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/decode(from:).md)
  Decodes a previously fitted transformer.
### Preprocesing and Fitting
- [func preprocessed<InputSequence, FeatureSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>]](preprocessingsupervisedtemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed annotated features.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], validateOn: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed examples while validating.
- [PreprocessingSupervisedTemporalEstimator.Annotation](preprocessingsupervisedtemporalestimator/annotation.md)
  The annotation type.
- [PreprocessingSupervisedTemporalEstimator.Input](preprocessingsupervisedtemporalestimator/input.md)
  The input type.
- [PreprocessingSupervisedTemporalEstimator.Intermediate](preprocessingsupervisedtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedTemporalEstimator.Output](preprocessingsupervisedtemporalestimator/output.md)
  The output type.
- [PreprocessingSupervisedTemporalEstimator.Transformer](preprocessingsupervisedtemporalestimator/transformer.md)
  The transformer type created by this estimator.
### Default Implementations
- [SupervisedTemporalEstimator Implementations](preprocessingsupervisedtemporalestimator/supervisedtemporalestimator-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SupervisedTemporalEstimator](supervisedtemporalestimator.md)

## See Also

- [struct PreprocessingEstimator](preprocessingestimator.md)
  An estimator that composes a preprocessing transformer and an estimator.
- [struct PreprocessingTemporalEstimator](preprocessingtemporalestimator.md)
  A temporal estimator that composes a preprocessing transformer and a temporal estimator.
- [struct PreprocessingSupervisedEstimator](preprocessingsupervisedestimator.md)
  A supervised estimator that composes a preprocessing transformer and a supervised estimator.
- [struct PreprocessingUpdatableEstimator](preprocessingupdatableestimator.md)
  An updatable estimator that composes a preprocessing transformer and an updatable estimator.
- [struct PreprocessingUpdatableTemporalEstimator](preprocessingupdatabletemporalestimator.md)
  An updatable temporal estimator that composes a preprocessing transformer and an updatable temporal estimator.
- [struct PreprocessingUpdatableSupervisedEstimator](preprocessingupdatablesupervisedestimator.md)
  An updatable supervised estimator that composes a preprocessing transformer and an updatable supervised estimator.
- [struct PreprocessingUpdatableSupervisedTemporalEstimator](preprocessingupdatablesupervisedtemporalestimator.md)
  An updatable supervised temporal estimator that composes a preprocessing transformer and an updatable supervised temporal estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtemporalestimator)*