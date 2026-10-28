# fitted(to:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Fits a transformer to a data frame

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
func fitted(to input: DataFrame, validateOn validation: DataFrame?, eventHandler: EventHandler? = nil) async throws -> PreprocessingSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer
```

## Return Value

The fitted transformer.

## Parameters

- `input`: A data frame containing examples used for fitting the transformer.
- `validation`: A data frame containing examples used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

### Preprocesing and fitting
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](./preprocessed%28from,eventhandler%29.md)
  Preprocesses a data frame of examples.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingsupervisedtabularestimator/fitted(to:validateon:eventhandler:))*