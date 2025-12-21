# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a sequence of examples while validating with a validation sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func fitted<InputSequence, Validation, FeatureSequence>(to input: InputSequence, validateOn validation: Validation, eventHandler: EventHandler? = nil) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer where InputSequence : Sequence, Validation : Sequence, FeatureSequence : TemporalSequence, Preprocessor.Input == FeatureSequence.Feature, InputSequence.Element == AnnotatedFeature<FeatureSequence, Estimator.Annotation>, Validation.Element == AnnotatedFeature<FeatureSequence, Estimator.Annotation>
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples used for fitting the transformer.
- `validation`: A sequence of examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed<InputSequence, FeatureSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>]](preprocessingupdatablesupervisedtemporalestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(to:eventhandler:).md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], validateOn: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features while validating.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtemporalestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtemporalestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, FeatureSequence>(inout PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: InputSequence, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtemporalestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new sequence of preprocessed features.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Annotation](preprocessingupdatablesupervisedtemporalestimator/annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Input](preprocessingupdatablesupervisedtemporalestimator/input.md)
  The input type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Intermediate](preprocessingupdatablesupervisedtemporalestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Output](preprocessingupdatablesupervisedtemporalestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator/fitted(to:validateon:eventhandler:))*