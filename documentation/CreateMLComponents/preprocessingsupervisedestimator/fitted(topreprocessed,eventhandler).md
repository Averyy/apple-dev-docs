# fitted(toPreprocessed:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Fits a transformer to a sequence of preprocessed features.

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
func fitted<S>(toPreprocessed preprocessed: S, eventHandler: EventHandler? = nil) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer where S : Sequence, S.Element == AnnotatedFeature<Preprocessor.Output, Estimator.Annotation>
```

## Return Value

The fitted transformer.

## Parameters

- `preprocessed`: A sequence of preprocessed features.
- `eventHandler`: An event handler.

## See Also

### Preprocessing and fitting
- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> AnySequence<AnnotatedFeature<Preprocessor.Output, PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Annotation>>](./preprocessed%28from,eventhandler%29.md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<InputSequence, Validation>(to: InputSequence, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,validateon,eventhandler%29.md)
  Fits a composed transformer to a sequence of examples.
- [func fitted<Input, Validation>(toPreprocessed: Input, validateOn: Validation, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Transformer](./fitted%28topreprocessed,validateon,eventhandler%29.md)
  Fits a composed transformer to a sequence of preprocessed features.
- [PreprocessingSupervisedEstimator.Annotation](./annotation.md)
  The annotation type.
- [PreprocessingSupervisedEstimator.Input](./input.md)
  The input type.
- [PreprocessingSupervisedEstimator.Intermediate](./intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedEstimator.Output](./output.md)
  The output type.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedestimator/fitted(topreprocessed:eventhandler:))*