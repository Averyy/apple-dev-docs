# predictions(fromBatch:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Generates predictions for each input feature provider within the batch provider.

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
func predictions(fromBatch inputBatch: any MLBatchProvider) throws -> any MLBatchProvider
```

```objc
- (id<MLBatchProvider>) predictionsFromBatch:(id<MLBatchProvider>) inputBatch error:(NSError **) error;
```

#### Return Value

A batch provider that contains an output feature provider for each prediction.

#### Discussion

Use this method to make more than one prediction at one time.

## Parameters

- `inputBatch`: A batch provider that contains multiple input feature providers. The model makes a prediction for each feature provider.

## See Also

### Making predictions
- [func prediction(from:)](./prediction%28from%29.md)
- [func prediction(from:options:)](./prediction%28from,options%29.md)
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](./predictions%28from,options%29.md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:)](./prediction%28from,using%29.md)
- [func prediction(from:using:options:)](./prediction%28from,using,options%29.md)
- [class MLPredictionOptions](../mlpredictionoptions.md)
  The options available when making a prediction.
- [Background Inference](../../BundleResources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/predictions(frombatch:))*