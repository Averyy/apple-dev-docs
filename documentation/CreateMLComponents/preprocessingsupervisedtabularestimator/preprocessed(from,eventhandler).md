# preprocessed(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Preprocesses a data frame of examples.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func preprocessed(from input: DataFrame, eventHandler: EventHandler? = nil) async throws -> DataFrame
```

## Return Value

The preprocessed examples.

## Parameters

- `input`: A data frame of examples.
- `eventHandler`: An event handler.

## See Also

### Preprocesing and fitting
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,validateon,eventhandler%29.md)
  Fits a transformer to a data frame
- [func fitted(toPreprocessed: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](./fitted%28topreprocessed,validateon,eventhandler%29.md)
  Fits a transformer to a data frame of preprocessed examples while validating.
- [PreprocessingSupervisedTabularEstimator.Annotation](./annotation.md)
  The annotation type.
- [PreprocessingSupervisedTabularEstimator.Input](./input.md)
  The input type.
- [PreprocessingSupervisedTabularEstimator.Intermediate](./intermediate.md)
  The intermediate type.
- [PreprocessingSupervisedTabularEstimator.Output](./output.md)
  The output type.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator/preprocessed(from:eventhandler:))*