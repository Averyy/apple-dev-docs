# update(_:withPreprocessed:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Updates a transformer with a new sequence of preprocessed features.

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
func update<InputSequence>(_ transformer: inout PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed preprocessed: InputSequence, eventHandler: EventHandler? = nil) async throws where InputSequence : Sequence, InputSequence.Element == AnnotatedFeature<Preprocessor.Output, Estimator.Annotation>
```

## Parameters

- `transformer`: A transformer to update.
- `preprocessed`: A sequence of preprocessed features.
- `eventHandler`: An event handler.

## See Also

### Preprocesing and fitting
- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> AnySequence<AnnotatedFeature<Preprocessor.Output, PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Annotation>>](./preprocessed%28from,eventhandler%29.md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<S>(toPreprocessed: S, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](./fitted%28topreprocessed,eventhandler%29.md)
  Fits a transformer to a sequence of preprocessed features.
- [func fitted<InputSequence, Validation>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,validateon,eventhandler%29.md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<InputSequence, Validation>(toPreprocessed: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](./fitted%28topreprocessed,validateon,eventhandler%29.md)
  Fits a composed transformer to a sequence of examples.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func update<InputSequence>(inout PreprocessingUpdatableSupervisedEstimator<Preprocessor, Estimator>.Transformer, with: InputSequence, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new sequence of examples.
- [PreprocessingUpdatableSupervisedEstimator.Annotation](./annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedEstimator.Input](./input.md)
  The input type.
- [PreprocessingUpdatableSupervisedEstimator.Intermediate](./intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedEstimator.Output](./output.md)
  The output type.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedestimator/update(_:withpreprocessed:eventhandler:))*