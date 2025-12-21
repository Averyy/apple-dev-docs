# fitted(to:eventHandler:)

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
func fitted(to input: DataFrame, eventHandler: EventHandler? = nil) async throws -> PreprocessingUpdatableTabularEstimator<Preprocessor, Estimator>.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A data frame of examples.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingupdatabletabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame of examples.
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
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingupdatabletabularestimator/fitted(to:eventhandler:))*