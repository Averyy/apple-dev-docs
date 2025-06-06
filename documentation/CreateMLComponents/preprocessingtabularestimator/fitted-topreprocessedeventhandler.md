# fitted(toPreprocessed:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a transformer to a data frame of preprocessed features.

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
func fitted(toPreprocessed preprocessed: DataFrame, eventHandler: EventHandler? = nil) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer
```

#### Return Value

The fitted transformer.

## Parameters

- `preprocessed`: A data frame of preprocessed features.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed(from: DataFrame, eventHandler: EventHandler?) async throws -> DataFrame](preprocessingtabularestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a data frame of examples.
- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [PreprocessingTabularEstimator.Input](preprocessingtabularestimator/input.md)
  The input type.
- [PreprocessingTabularEstimator.Intermediate](preprocessingtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTabularEstimator.Output](preprocessingtabularestimator/output.md)
  The output type.
- [PreprocessingTabularEstimator.Transformer](preprocessingtabularestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtabularestimator/fitted(topreprocessed:eventhandler:))*