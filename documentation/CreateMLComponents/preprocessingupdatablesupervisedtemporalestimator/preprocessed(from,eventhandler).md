# preprocessed(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Preprocesses a sequence of examples.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func preprocessed<InputSequence, FeatureSequence>(from input: InputSequence, eventHandler: EventHandler? = nil) async throws -> [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>] where InputSequence : Sequence, FeatureSequence : TemporalSequence, Preprocessor.Input == FeatureSequence.Feature, InputSequence.Element == AnnotatedFeature<FeatureSequence, Estimator.Annotation>
```

## Return Value

The preprocessed examples.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

### Preprocesing and fitting
- [func fitted<InputSequence, FeatureSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](./fitted%28topreprocessed,eventhandler%29.md)
  Fits a transformer to a sequence of preprocessed features.
- [func fitted<InputSequence, Validation, FeatureSequence>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of examples while validating with a validation sequence.
- [func fitted(toPreprocessed: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], validateOn: [AnnotatedFeature<PreprocessedFeatureSequence<Preprocessor.Output>, PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Annotation>], eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](./fitted%28topreprocessed,validateon,eventhandler%29.md)
  Fits a transformer to a sequence of preprocessed features while validating.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence, FeatureSequence>(inout PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.
- [func update<InputSequence, FeatureSequence>(inout PreprocessingUpdatableSupervisedTemporalEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,withpreprocessed,eventhandler%29.md)
  Updates a transformer with a new sequence of preprocessed features.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Annotation](./annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Input](./input.md)
  The input type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Intermediate](./intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedTemporalEstimator.Output](./output.md)
  The output type.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtemporalestimator/preprocessed(from:eventhandler:))*