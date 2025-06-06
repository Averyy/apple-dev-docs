# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Accesses a contiguous range of elements with a range expression.

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
subscript<R>(range: R) -> ColumnSlice<WrappedElement> where R : RangeExpression, R.Bound == Int { get set }
```

## Parameters

- `range`: An integer range expression that represents valid indices in the column.

## See Also

- [subscript(Int) -> Column<WrappedElement>.Element](column/subscript(_:)-qm4d.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](column/subscript(_:)-gne9.md)
  Accesses a contiguous range of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/subscript(_:)-52xy1)*