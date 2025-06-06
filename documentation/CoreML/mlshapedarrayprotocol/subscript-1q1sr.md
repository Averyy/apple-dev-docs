# subscript(_:)

**Framework**: Core ML  
**Kind**: subscript  
**Required**: Yes

Accesses a slice using a collection of integer ranges, in which each element is a range in the corresponding dimension.

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
subscript<C>(sliceRanges: C) -> MLShapedArraySlice<Self.Scalar> where C : Collection, C.Element == Range<Int> { get set }
```

## See Also

- [subscript<C>(scalarAt _: C) -> Self.Scalar](mlshapedarrayprotocol/subscript(scalarat:).md)
  Accesses an element and a multidimensional location.
- [subscript<C>(C) -> MLShapedArraySlice<Self.Scalar>](mlshapedarrayprotocol/subscript(_:)-zfw5.md)
  Accesses a slice using a collection of integers, in which each element is an index in the corresponding dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(_:)-1q1sr)*