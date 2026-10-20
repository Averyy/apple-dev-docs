# prediction(from:using:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func prediction(from inputs: [String : MLTensor], using state: MLState) async throws -> [String : MLTensor]
```

## See Also

### Making predictions
- [func prediction(from:)](./prediction%28from%29.md)
- [func prediction(from:options:)](./prediction%28from,options%29.md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](./predictions%28frombatch%29.md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](./predictions%28from,options%29.md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:options:)](./prediction%28from,using,options%29.md)
- [class MLPredictionOptions](../mlpredictionoptions.md)
  The options available when making a prediction.
- [Background Inference](../../BundleResources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:using:))*