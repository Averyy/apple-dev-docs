# prediction(from:options:)

**Framework**: Core ML  
**Kind**: method  
**Required**: Yes

Predicts output values from the given input features.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider
```

#### Return Value

A feature provider that represents the model’s prediction.

## Parameters

- `input`: The feature values the models needs to make its prediction.
- `options`: The options to be applied to the prediction.

## See Also

- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](mlcustommodel/predictions(from:options:).md)
  Predicts output values from the given batch of input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustommodel/prediction(from:options:))*