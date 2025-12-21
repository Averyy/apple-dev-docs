# fitted(toPreprocessed:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a sequence of preprocessed examples while validating.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fitted(toPreprocessed preprocessedInput: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], validateOn preprocessedValidation: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler? = nil) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `preprocessedInput`: A sequence of preprocessed features used for fitting the transformer.
- `preprocessedValidation`: A sequence of preprocessed features used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed<InputSequence, FeatureSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>]](preprocessingsupervisedtemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed annotated features.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingsupervisedtemporalestimator/fitted(to:validateon:eventhandler:).md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [PreprocessingSupervisedTemporalEstimator.Annotation](preprocessingsupervisedtemporalestimator/annotation.md)
  The annotation type.
- [PreprocessingSupervisedTemporalEstimator.Input](preprocessingsupervisedtemporalestimator/input.md)
  The input type.
- [PreprocessingSupervisedTemporalEstimator.Intermediate](preprocessingsupervisedtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedTemporalEstimator.Output](preprocessingsupervisedtemporalestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtemporalestimator/fitted(topreprocessed:validateon:eventhandler:))*