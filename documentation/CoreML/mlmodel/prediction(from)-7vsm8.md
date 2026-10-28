# prediction(from:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Run a prediction on a model.

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
func prediction(from inputs: [String : MLTensor]) async throws -> [String : MLTensor]
```

**Other overloads**:

```swift
func prediction(from input: any MLFeatureProvider) throws -> any MLFeatureProvider
```

## Return Value

The output, or outputs, from the prediction.

## Discussion

This method requires all inputs and outputs to be multidimensional arrays. If your model doesn’t satisfy this requirement, materialize the tensor inputs to `MLShapedArray` values to create feature values for each, for example:

```swift
let shapedArray = await tensor.shapedArray(of: Float.self)
let inputFeatures = try MLDictionaryFeatureProvider(dictionary: [
    "x": MLFeatureValue(shapedArray: shapedArray),
    // Other non-multidimensional array inputs
])
let prediction = try await model.prediction(from: inputFeatures)
```

## Parameters

- `inputs`: The named input, or inputs, to make a prediction from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/prediction(from:)-7vsm8)*