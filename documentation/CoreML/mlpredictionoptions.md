# MLPredictionOptions

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

The options available when making a prediction.

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
class MLPredictionOptions
```

```objc
@interface MLPredictionOptions : NSObject
```

## Topics

### Getting features
- [var outputBackings: [String : Any]](./mlpredictionoptions/outputbackings.md)
  A dictionary of feature names and client-allocated buffers.
### Restricting computation to the CPU
- [var usesCPUOnly: Bool](./mlpredictionoptions/usescpuonly.md)
  A Boolean value that indicates whether a prediction is computed using only the CPU.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Making predictions
- [func prediction(from:)](./mlmodel/prediction%28from%29.md)
- [func prediction(from:options:)](./mlmodel/prediction%28from,options%29.md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](./mlmodel/predictions%28frombatch%29.md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](./mlmodel/predictions%28from,options%29.md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:)](./mlmodel/prediction%28from,using%29.md)
- [func prediction(from:using:options:)](./mlmodel/prediction%28from,using,options%29.md)
- [Background Inference](../BundleResources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlpredictionoptions)*