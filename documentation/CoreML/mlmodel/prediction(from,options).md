# prediction(from:options:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

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
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider
```

**Other overloads**:

```swift
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions = MLPredictionOptions()) async throws -> any MLFeatureProvider
```

## See Also

### Making predictions
- [func prediction(from:)](./prediction%28from%29.md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](./predictions%28frombatch%29.md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](./predictions%28from,options%29.md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:)](./prediction%28from,using%29.md)
- [func prediction(from:using:options:)](./prediction%28from,using,options%29.md)
- [class MLPredictionOptions](../mlpredictionoptions.md)
  The options available when making a prediction.
- [Background Inference](../../BundleResources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:options:))*