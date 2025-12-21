# subscript(_:)

**Framework**: Core ML  
**Kind**: subscript  
**Required**: Yes

A slice of the shaped array for the selected leading axes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
subscript<C>(indices: C) -> MLShapedArraySlice<Self.Scalar> where C : Collection, C.Element == Int { get set }
```

#### Overview

The slice has a rank of `self.rank - indices.count`. For example, given a shaped array `m` with the shape being `3 x 3`, `m[[1]]` returns a slice of shape `[3]` with the contents labeld as `x` below.

```None
 O  O  O
 x  x  x
 O  O  O
```

## Parameters

- `indices`: The indices to slice the array.

## See Also

- [subscript<C>(scalarAt _: C) -> Self.Scalar](mlshapedarrayprotocol/subscript(scalarat:).md)
  Accesses an element and a multidimensional location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(_:))*