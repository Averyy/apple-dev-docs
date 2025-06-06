# fitted(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Fits a composed transformer to a sequence of examples.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func fitted<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer where S : Sequence, Preprocessor.Input == S.Element
```

#### Return Value

The fitted transformer.

## Parameters

- `input`: A sequence of examples.
- `eventHandler`: An event handler.

## See Also

- [func preprocessed<S>(from: S, eventHandler: EventHandler?) async throws -> [Preprocessor.Output]](preprocessingestimator/preprocessed(from:eventhandler:).md)
  Preprocesses a sequence of examples.
- [func fitted<S>(toPreprocessed: S, eventHandler: EventHandler?) async throws -> PreprocessingEstimator<Preprocessor, Estimator>.Transformer](preprocessingestimator/fitted(topreprocessed:eventhandler:).md)
  Fits a transformer to a sequence of preprocessed features.
- [PreprocessingEstimator.Input](preprocessingestimator/input.md)
  The input type.
- [PreprocessingEstimator.Intermediate](preprocessingestimator/intermediate.md)
  The intermediate type.
- [PreprocessingEstimator.Output](preprocessingestimator/output.md)
  The output type.
- [PreprocessingEstimator.Transformer](preprocessingestimator/transformer.md)
  The transformer type created by this estimator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/preprocessingestimator/fitted(to:eventhandler:))*