# preprocessed(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Preprocesses a sequence of examples.

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
func preprocessed<S>(from input: S, eventHandler: EventHandler? = nil) async throws -> AnySequence<AnnotatedFeature<Preprocessor.Output, PreprocessingSupervisedEstimator<Preprocessor, Estimator>.Annotation>> where S : Sequence, S.Element == AnnotatedFeature<Preprocessor.Input, Estimator.Annotation>
```

#### Return Value

The preprocessed examples.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedestimator/preprocessed(from:eventhandler:))*