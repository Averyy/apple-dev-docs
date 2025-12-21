# preprocessed(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Preprocesses a data frame.

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

#### Return Value

The preprocessed examples.

## Parameters

- `input`: A data frame of examples.
- `eventHandler`: An event handler.

## See Also

- [func fitted(to: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(to:validateon:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, validateOn: DataFrame?, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/fitted(topreprocessed:validateon:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func makeTransformer() -> PreprocessingUpdatableSupervisedTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatablesupervisedtabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
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
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatablesupervisedtabularestimator/preprocessed(from:eventhandler:))*