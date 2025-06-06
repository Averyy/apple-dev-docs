# prediction(from:using:options:)

**Framework**: Core ML  
**Kind**: method

Run a stateful prediction on a model asynchronously.

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
func prediction(from input: any MLFeatureProvider, using state: MLState, options: MLPredictionOptions = MLPredictionOptions()) async throws -> any MLFeatureProvider
```

#### Return Value

The output from the prediction.

#### Discussion

```swift
let state = model.newState()
let prediction = try await model.prediction(from: inputFeatures, using: state)
```

## Parameters

- `input`: The input features to make a prediction from.
- `state`: The state.
- `options`: Optional prediction options to modify how the prediction is run

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
- [func prediction(from: any MLFeatureProvider, using: MLState, options: MLPredictionOptions) throws -> any MLFeatureProvider](mlmodel/prediction(from:using:options:)-v4wp.md)
  Run a stateful prediction synchronously with options.
- [class MLPredictionOptions](mlpredictionoptions.md)
  The options available when making a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:using:options:)-8b4qa)*