# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Accesses a contiguous range of elements.

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
subscript(bounds: Range<Int>) -> ColumnSlice<WrappedElement> { get set }
```

## Parameters

- `bounds`: A range of valid indices in the column.

## See Also

- [subscript(Int) -> Column<WrappedElement>.Element](column/subscript(_:)-qm4d.md)
  Accesses an element at an index.
- [subscript<R>(R) -> ColumnSlice<WrappedElement>](column/subscript(_:)-52xy1.md)
  Accesses a contiguous range of elements with a range expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/subscript(_:)-gne9)*