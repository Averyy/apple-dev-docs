# prediction(from:using:options:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func prediction(from inputFeatures: any MLFeatureProvider, using state: MLState, options: MLPredictionOptions) throws -> any MLFeatureProvider
```

## Return Value

The output from the prediction.

## Discussion

```swift
let state = model.newState()
let prediction = try await model.prediction(from: inputFeatures, using: state)
```

## Parameters

- `input`: The input features to make a prediction from.
- `state`: The state.
- `options`: Optional prediction options to modify how the prediction is run


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:using:options:)-8b4qa)*