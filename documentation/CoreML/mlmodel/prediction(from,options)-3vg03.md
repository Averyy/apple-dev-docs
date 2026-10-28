# prediction(from:options:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Generates a prediction asynchronously from the feature values within the input feature provider using the prediction options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions = MLPredictionOptions()) async throws -> any MLFeatureProvider
```

**Other overloads**:

```swift
func prediction(from input: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider
```

## Return Value

A feature provider that contains the outputs of the prediction.

## Discussion

Use this method to make a single prediction.

## Parameters

- `input`: A feature provider that stores all the input feature values the model needs for a prediction.
- `options`: The runtime settings the model uses as it makes a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:options:)-3vg03)*