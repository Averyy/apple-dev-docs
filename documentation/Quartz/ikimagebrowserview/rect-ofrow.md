# rect(ofRow:)

**Framework**: Quartz  
**Kind**: method

Returns the rectangle containing the specified row.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func rect(ofRow rowIndex: Int) -> NSRect
```

#### Return Value

A rectangle containing the column. Specified in the view’s coordinate system.

## Parameters

- `rowIndex`: The row index.

## See Also

- [func numberOfColumns() -> Int](ikimagebrowserview/numberofcolumns.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](ikimagebrowserview/numberofrows.md)
  Returns the current number of rows.
- [func rect(ofColumn: Int) -> NSRect](ikimagebrowserview/rect(ofcolumn:).md)
  Returns the rectangle containing the specified column.
- [func columnIndexes(in: NSRect) -> IndexSet!](ikimagebrowserview/columnindexes(in:).md)
  Returns the column indexes in the specified rectangle.
- [func rowIndexes(in: NSRect) -> IndexSet!](ikimagebrowserview/rowindexes(in:).md)
  Returns the row indexes in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/rect(ofrow:))*