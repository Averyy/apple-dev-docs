# prediction(from:)

**Framework**: Core ML  
**Kind**: method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func prediction(from input: any MLFeatureProvider) throws -> any MLFeatureProvider
```

## See Also

- [func prediction(from:options:)](mlmodel/prediction(from:options:).md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](mlmodel/predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:)](mlmodel/prediction(from:using:).md)
- [func prediction(from:using:options:)](mlmodel/prediction(from:using:options:).md)
- [class MLPredictionOptions](mlpredictionoptions.md)
  The options available when making a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:))*