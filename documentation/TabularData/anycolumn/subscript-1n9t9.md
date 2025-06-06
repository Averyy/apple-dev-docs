# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Accesses a contiguous subrange of the elements.

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
subscript(range: Range<Int>) -> AnyColumnSlice { get set }
```

## Parameters

- `range`: A range of valid indices in the column.

## See Also

- [subscript(Int) -> Any?](anycolumn/subscript(_:)-6z1b5.md)
  Accesses an element at an index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn/subscript(_:)-1n9t9)*