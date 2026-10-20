# subscript(scalarAt:)

**Framework**: Core ML  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Accesses an element and a multidimensional location.

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
subscript<C>(scalarAt indices: C) -> Self.Scalar where C : Collection, C.Element == Int { get set }
```

## Parameters

- `indices`: An integer collection that represents a position in the shaped array in which each integer is an index in the corresponding dimension.

## Default Implementations

### MLShapedArrayProtocol Implementations
- [subscript(scalarAt _: Int...) -> Self.Scalar](./subscript%28scalarat%29-6yvwm.md)
  The scalar value at the indices.

## See Also

### Accessing elements
- [subscript(_:)](./subscript%28_%29.md)
  A slice of the shaped array for the selected leading axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(scalarat:))*