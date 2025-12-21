# subscript(scalarAt:)

**Framework**: Core ML  
**Kind**: subscript  
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

## See Also

- [subscript(_:)](mlshapedarrayprotocol/subscript(_:).md)
  A slice of the shaped array for the selected leading axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlshapedarrayprotocol/subscript(scalarat:))*