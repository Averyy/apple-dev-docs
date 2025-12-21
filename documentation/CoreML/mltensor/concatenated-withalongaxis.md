# concatenated(with:alongAxis:)

**Framework**: Core ML  
**Kind**: method

Returns a concatenated tensor along the specified axis.

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
func concatenated(with other: MLTensor, alongAxis axis: Int = 0) -> MLTensor
```

## Parameters

- `other`: The tensor to concatenate. The tensors must have the same dimensions, except for the specified axis.
- `axis`: The axis along which to concatenate. Negative values wrap around but must be in the range  .

## See Also

- [func clamped(to:)](mltensor/clamped(to:).md)
  Clamps all elements to the given lower and upper bounds, inclusively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/concatenated(with:alongaxis:))*