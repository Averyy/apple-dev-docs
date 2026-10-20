# fitted(toPreprocessed:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Fits a composed transformer to a data frame of examples.

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
func fitted(toPreprocessed preprocessedInput: DataFrame, validateOn preprocessedValidation: DataFrame?, eventHandler: EventHandler? = nil) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `preprocessedInput`: A data frame of preprocessed features used for fitting the transformer.
- `preprocessedValidation`: A data frame of preprocessed features used for validating the fitted transformer.
- `eventHandler`: An event handler.

## See Also

### Preprocesing and fitting
- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](./fitted%28to,validateon,eventhandler%29.md)
  Fits a composed transformer to a data frame of examples.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](./maketransformer%28%29.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](./preprocessed%28from,eventhandler%29.md)
  Preprocesses a data frame.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](./update%28_,with,eventhandler%29.md)
  Updates a transformer with a new data frame of examples.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: DataFrame, eventHandler: EventHandler?) async throws](./update%28_,withpreprocessed,eventhandler%29.md)
  Updates a transformer with a new data frame of preprocessed features.
- [PreprocessingUpdatableSupervisedTabularEstimator.Annotation](./annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Input](./input.md)
  The input type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Intermediate](./intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Output](./output.md)
  The output type.
- [protocol Transformer](../transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:))*