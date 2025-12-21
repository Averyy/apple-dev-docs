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

- [func fitted(to: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/fitted(to:eventhandler:).md)
  Fits a composed transformer to a data frame of examples.
- [func fitted(toPreprocessed: DataFrame, eventHandler: EventHandler?) async throws -> PreprocessingTabularEstimator<Preprocessor, Estimator>.Transformer](preprocessingtabularestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a data frame of preprocessed features.
- [PreprocessingTabularEstimator.Input](preprocessingtabularestimator/input.md)
  The input type.
- [PreprocessingTabularEstimator.Intermediate](preprocessingtabularestimator/intermediate.md)
  The intermediate type.
- [PreprocessingTabularEstimator.Output](preprocessingtabularestimator/output.md)
  The output type.
- [protocol Transformer](transformer.md)
  A transformer that takes an input and produces an output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingtabularestimator/preprocessed(from:eventhandler:))*