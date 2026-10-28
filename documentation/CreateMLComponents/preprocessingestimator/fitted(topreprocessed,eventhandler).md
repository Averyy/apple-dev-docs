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
func fitted<S>(toPreprocessed preprocessed: S, eventHandler: EventHandler? = nil) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer where S : Sequence, Preprocessor.Output == S.Element, S.Element == Estimator.Transformer.Input
```

## Return Value

The fitted transformer.

## Parameters

- `preprocessed`: A sequence of preprocessed features.
- `eventHandler`: An event handler.

## See Also

### Preprocesing and fitting
- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> [Preprocessor.Output]](./preprocessed%28from,eventhandler%29.md)
  Preprocesses a sequence of examples.
- [func fitted<S>(to: S, eventHandler: EventHandler?) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a composed transformer to a sequence of examples.
- [PreprocessingEstimator.Input](./input.md)
  The input type.
- [PreprocessingEstimator.Intermediate](./intermediate.md)
  The intermediate type.
- [PreprocessingEstimator.Output](./output.md)
  The output type.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingestimator/fitted(topreprocessed:eventhandler:))*