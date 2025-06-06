# rowIndexes(in:)

**Framework**: Quartz  
**Kind**: method

Returns the row indexes in the specified rectangle.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func rowIndexes(in rect: NSRect) -> IndexSet!
```

#### Return Value

An index set containing the item indexes.

## Parameters

- `rect`: A rectangle in the view’s coordinate system.

## See Also

- [func numberOfColumns() -> Int](ikimagebrowserview/numberofcolumns.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](ikimagebrowserview/numberofrows.md)
  Returns the current number of rows.
- [func rect(ofColumn: Int) -> NSRect](ikimagebrowserview/rect(ofcolumn:).md)
  Returns the rectangle containing the specified column.
- [func columnIndexes(in: NSRect) -> IndexSet!](ikimagebrowserview/columnindexes(in:).md)
  Returns the column indexes in the specified rectangle.
- [func rect(ofRow: Int) -> NSRect](ikimagebrowserview/rect(ofrow:).md)
  Returns the rectangle containing the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/rowindexes(in:))*