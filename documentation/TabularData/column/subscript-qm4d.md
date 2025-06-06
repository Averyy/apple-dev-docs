# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Accesses an element at an index.

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
subscript(position: Int) -> Column<WrappedElement>.Element { get set }
```

## Parameters

- `position`: A valid index to an element in the column.

## See Also

- [subscript<R>(R) -> ColumnSlice<WrappedElement>](column/subscript(_:)-52xy1.md)
  Accesses a contiguous range of elements with a range expression.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](column/subscript(_:)-gne9.md)
  Accesses a contiguous range of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/subscript(_:)-qm4d)*