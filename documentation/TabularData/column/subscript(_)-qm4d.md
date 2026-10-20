# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript  
**Role**: Instance Subscript

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

### Accessing Elements
- [subscript<R>(R) -> ColumnSlice<WrappedElement>](./subscript%28_%29-52xy1.md)
  Accesses a contiguous range of elements with a range expression.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](./subscript%28_%29-gne9.md)
  Accesses a contiguous range of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/subscript(_:)-qm4d)*