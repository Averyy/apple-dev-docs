# InferenceFunction.Outputs

**Framework**: Core AI  
**Kind**: struct

The output values produced by running an inference function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Outputs
```

## Topics

### Accessing outputs
- [func remove(String) -> InferenceValue?](inferencefunction/outputs/remove(_:).md)
  Removes and returns the output value with the specified name.
- [var count: Int](inferencefunction/outputs/count.md)
  The number of outputs in this collection.
- [var names: some Collection<String>](inferencefunction/outputs/names.md)
  The names of the outputs in this collection.

## See Also

- [InferenceFunction.Inputs](inferencefunction/inputs.md)
  A collection of named input values for an inference function.
- [InferenceFunction.MutableViews](inferencefunction/mutableviews.md)
  A collection of `InferenceValue.MutableView`s which can be updated in-place by an `InferenceFunction`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/outputs)*