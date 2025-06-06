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

- [func prediction(from: any MLFeatureProvider) throws -> any MLFeatureProvider](mlmodel/prediction(from:)-9y2aa.md)
  Generates a prediction from the feature values within the input feature provider.
- [func prediction(from: [String : MLTensor]) async throws -> [String : MLTensor]](mlmodel/prediction(from:)-7vsm8.md)
  Run a prediction on a model.
- [func prediction(from: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider](mlmodel/prediction(from:options:)-81mr6.md)
  Generates a prediction from the feature values within the input feature provider using the prediction options.
- [func prediction(from: any MLFeatureProvider, options: MLPredictionOptions) async throws -> any MLFeatureProvider](mlmodel/prediction(from:options:)-3vg03.md)
  Generates a prediction asynchronously from the feature values within the input feature provider using the prediction options.
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](mlmodel/predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from: [String : MLTensor], using: MLState) async throws -> [String : MLTensor]](mlmodel/prediction(from:using:)-6whkh.md)
  Run a stateful prediction on a model.
- [func prediction(from: any MLFeatureProvider, using: MLState) throws -> any MLFeatureProvider](mlmodel/prediction(from:using:)-97bu1.md)
  Run a stateful prediction synchronously.
- [func prediction(from: any MLFeatureProvider, using: MLState, options: MLPredictionOptions) async throws -> any MLFeatureProvider](mlmodel/prediction(from:using:options:)-8b4qa.md)
  Run a stateful prediction on a model asynchronously.
- [func prediction(from: any MLFeatureProvider, using: MLState, options: MLPredictionOptions) throws -> any MLFeatureProvider](mlmodel/prediction(from:using:options:)-v4wp.md)
  Run a stateful prediction synchronously with options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlpredictionoptions)*