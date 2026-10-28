# fitted(toPreprocessed:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Fits a transformer to a sequence of preprocessed features.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
func fitted(toPreprocessed preprocessed: [PreprocessedFeatureSequence<Preprocessor.Output>], eventHandler: EventHandler? = nil) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer
```

## Return Value

The fitted transformer.

## Parameters

- `preprocessed`: A sequence of preprocessed featuress.
- `eventHandler`: An event handler.

## See Also

### Preprocesing and fitting
- [func preprocessed<InputSequence>(from: InputSequence, eventHandler: EventHandler?) async throws -> [PreprocessedFeatureSequence<Preprocessor.Output>]](./preprocessed%28from,eventhandler%29.md)
  Preprocesses a sequence of examples.
- [func fitted<InputSequence>(to: InputSequence, eventHandler: EventHandler?) async throws -> PreprocessingTemporalEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,eventhandler%29.md)
  Fits a transformer to a sequence of examples.
- [PreprocessingTemporalEstimator.Input](./input.md)
  The input type.
- [PreprocessingTemporalEstimator.Intermediate](./intermediate.md)
  The intermediate type.
- [PreprocessingTemporalEstimator.Output](./output.md)
  The output type.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtemporalestimator/fitted(topreprocessed:eventhandler:))*