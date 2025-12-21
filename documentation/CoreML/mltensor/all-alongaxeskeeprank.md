# all(alongAxes:keepRank:)

**Framework**: Core ML  
**Kind**: method

Computes logical AND on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.

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
func all(alongAxes axes: Int..., keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced Boolean tensor.

## Parameters

- `axes`: The axes to reduce.
- `keepRank`: A Boolean indicating whether to keep the reduced axes or not. The default value is  .

## See Also

- [func all(keepRank: Bool) -> MLTensor](mltensor/all(keeprank:).md)
  Computes logical AND on elements across all axes of a tensor where the scalar type of the tensor is expected to be Boolean.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/all(alongaxes:keeprank:))*