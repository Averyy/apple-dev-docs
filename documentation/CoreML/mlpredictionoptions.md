# MLPredictionOptions

**Framework**: Core ML  
**Kind**: class

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

## Topics

### Getting features
- [var outputBackings: [String : Any]](mlpredictionoptions/outputbackings.md)
  A dictionary of feature names and client-allocated buffers.
### Restricting computation to the CPU
- [var usesCPUOnly: Bool](mlpredictionoptions/usescpuonly.md)
  A Boolean value that indicates whether a prediction is computed using only the CPU.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func prediction(from:)](mlmodel/prediction(from:).md)
- [func prediction(from:options:)](mlmodel/prediction(from:options:).md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](mlmodel/predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:)](mlmodel/prediction(from:using:).md)
- [func prediction(from:using:options:)](mlmodel/prediction(from:using:options:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlpredictionoptions)*