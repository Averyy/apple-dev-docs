# prediction(from:using:)

**Framework**: Core ML  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func prediction(from inputFeatures: any MLFeatureProvider, using state: MLState) throws -> any MLFeatureProvider
```

## See Also

- [func prediction(from:)](mlmodel/prediction(from:).md)
- [func prediction(from:options:)](mlmodel/prediction(from:options:).md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](mlmodel/predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:options:)](mlmodel/prediction(from:using:options:).md)
- [class MLPredictionOptions](mlpredictionoptions.md)
  The options available when making a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:using:))*