# predictions(from:options:)

**Framework**: Core ML  
**Kind**: method

Generates a prediction for each input feature provider within the batch provider using the prediction options.

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
func predictions(from inputBatch: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider
```

#### Return Value

A batch provider that contains an output feature provider for each prediction.

#### Discussion

Use this method to make more than one prediction at one time.

## Parameters

- `inputBatch`: A batch provider that contains multiple input feature providers. The model makes a prediction for each feature provider.
- `options`: The runtime settings the model uses as it makes a prediction.

## See Also

- [func prediction(from:)](mlmodel/prediction(from:).md)
- [func prediction(from:options:)](mlmodel/prediction(from:options:).md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.
- [func prediction(from:using:)](mlmodel/prediction(from:using:).md)
- [func prediction(from:using:options:)](mlmodel/prediction(from:using:options:).md)
- [class MLPredictionOptions](mlpredictionoptions.md)
  The options available when making a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/predictions(from:options:))*