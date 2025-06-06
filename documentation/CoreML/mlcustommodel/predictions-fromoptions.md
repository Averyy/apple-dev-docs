# predictions(from:options:)

**Framework**: Core ML  
**Kind**: method

Predicts output values from the given batch of input features.

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
optional func predictions(from inputBatch: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider
```

#### Return Value

A batch provider that represents the model’s predictions for the batch of inputs.

## Parameters

- `inputBatch`: The batch of feature values the model needs to make its predictions.
- `options`: The options to be applied to the predictions.

## See Also

- [func prediction(from: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider](mlcustommodel/prediction(from:options:).md)
  Predicts output values from the given input features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcustommodel/predictions(from:options:))*