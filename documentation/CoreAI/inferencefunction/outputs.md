# InferenceFunction.Outputs

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

The output values produced by running an inference function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Outputs
```

## Topics

### Accessing outputs
- [func remove(String) -> InferenceValue?](./outputs/remove%28_%29.md)
  Removes and returns the output value with the specified name.
- [var count: Int](./outputs/count.md)
  The number of outputs in this collection.
- [var names: some Collection<String>](./outputs/names.md)
  The names of the outputs in this collection.

## See Also

### Supporting types
- [InferenceFunction.Inputs](./inputs.md)
  A collection of named input values for an inference function.
- [InferenceFunction.MutableViews](./mutableviews.md)
  A collection of `InferenceValue.MutableView`s which can be updated in-place by an `InferenceFunction`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/outputs)*