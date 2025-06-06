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
- [func prediction(from: [String : MLTensor], using: MLState) async throws -> [String : MLTensor]](mlmodel/prediction(from:using:)-6whkh.md)
  Run a stateful prediction on a model.
- [func prediction(from: any MLFeatureProvider, using: MLState) throws -> any MLFeatureProvider](mlmodel/prediction(from:using:)-97bu1.md)
  Run a stateful prediction synchronously.
- [func prediction(from: any MLFeatureProvider, using: MLState, options: MLPredictionOptions) async throws -> any MLFeatureProvider](mlmodel/prediction(from:using:options:)-8b4qa.md)
  Run a stateful prediction on a model asynchronously.
- [func prediction(from: any MLFeatureProvider, using: MLState, options: MLPredictionOptions) throws -> any MLFeatureProvider](mlmodel/prediction(from:using:options:)-v4wp.md)
  Run a stateful prediction synchronously with options.
- [class MLPredictionOptions](mlpredictionoptions.md)
  The options available when making a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/predictions(from:options:))*