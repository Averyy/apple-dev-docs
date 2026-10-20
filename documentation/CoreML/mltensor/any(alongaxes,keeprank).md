# any(alongAxes:keepRank:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Computes logical OR on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.

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
func any(alongAxes axes: Int..., keepRank: Bool = false) -> MLTensor
```

**Other overloads**:

```swift
func any(alongAxes axes: [Int], keepRank: Bool = false) -> MLTensor
```

#### Return Value

The reduced Boolean tensor.

## Parameters

- `axes`: The axes to reduce.
- `keepRank`: A Boolean indicating whether to keep the reduced axes or not. The default value is `false`.

## See Also

### Performing a logical OR operation
- [func any(keepRank: Bool) -> MLTensor](./any%28keeprank%29.md)
  Computes logical OR on elements across all dimensions of a tensor where the scalar type of the tensor is expected to be Boolean.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/any(alongaxes:keeprank:))*