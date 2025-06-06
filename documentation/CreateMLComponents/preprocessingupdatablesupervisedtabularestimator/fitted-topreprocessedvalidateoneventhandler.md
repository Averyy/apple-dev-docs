# fitted(toPreprocessed:validateOn:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

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

- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingupdatablesupervisedtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame of examples.
- [func update(inout PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatablesupervisedtabularestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new data frame of preprocessed features.
- [PreprocessingUpdatableSupervisedTabularEstimator.Annotation](preprocessingupdatablesupervisedtabularestimator/annotation.md)
  The annotation type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Input](preprocessingupdatablesupervisedtabularestimator/input.md)
  The input type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Intermediate](preprocessingupdatablesupervisedtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Output](preprocessingupdatablesupervisedtabularestimator/output.md)
  The output type.
- [PreprocessingUpdatableSupervisedTabularEstimator.Transformer](preprocessingupdatablesupervisedtabularestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:))*