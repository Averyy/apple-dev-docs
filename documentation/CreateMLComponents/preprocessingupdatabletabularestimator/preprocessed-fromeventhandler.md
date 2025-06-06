# preprocessed(from:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

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

#### Return Value

The preprocessed examples.

## Parameters

- `input`: A data frame of examples.
- `eventHandler`: An event handler.

## See Also

- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed features.
- [func update(inout PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer, with: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatabletabularestimator/update(_:with:eventhandler:).md)
  Updates a transformer with a new data frame of examples.
- [func update(inout PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer, withPreprocessed: DataFrame, eventHandler: EventHandler?) async throws](preprocessingupdatabletabularestimator/update(_:withpreprocessed:eventhandler:).md)
  Updates a transformer with a new data frame of preprocessed features.
- [func makeTransformer() -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingupdatabletabularestimator/maketransformer.md)
  Creates a default-initialized transformer suitable for incremental fitting.
- [PreprocessingUpdatableTabularEstimator.Input](preprocessingupdatabletabularestimator/input.md)
  The input type.
- [PreprocessingUpdatableTabularEstimator.Intermediate](preprocessingupdatabletabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingUpdatableTabularEstimator.Output](preprocessingupdatabletabularestimator/output.md)
  The output type.
- [PreprocessingUpdatableTabularEstimator.Transformer](preprocessingupdatabletabularestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletabularestimator/preprocessed(from:eventhandler:))*