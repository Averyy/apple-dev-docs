# prediction(from:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Generates a prediction from the feature values within the input feature provider.

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
func prediction(from input: any MLFeatureProvider) throws -> any MLFeatureProvider
```

```objc
- (id<MLFeatureProvider>) predictionFromFeatures:(id<MLFeatureProvider>) input error:(NSError **) error;
```

**Other overloads**:

```swift
func prediction(from inputs: [String : MLTensor]) async throws -> [String : MLTensor]
```

## Mentions

- [Creating and Integrating a Model with Custom Layers](../creating-and-integrating-a-model-with-custom-layers.md)

## Return Value

A feature provider that contains the outputs of the prediction.

## Discussion

Use this method to make a single prediction.

## Parameters

- `input`: A feature provider that stores all the input feature values the model needs for a prediction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:)-9y2aa)*