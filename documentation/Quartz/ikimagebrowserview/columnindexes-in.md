# columnIndexes(in:)

**Framework**: Quartz  
**Kind**: method

Returns the column indexes in the specified rectangle.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func columnIndexes(in rect: NSRect) -> IndexSet!
```

#### Return Value

An index set containing the cell indexes.

## Parameters

- `rect`: The rectangle in the view’s coordinate system.

## See Also

- [func numberOfColumns() -> Int](ikimagebrowserview/numberofcolumns.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](ikimagebrowserview/numberofrows.md)
  Returns the current number of rows.
- [func rect(ofColumn: Int) -> NSRect](ikimagebrowserview/rect(ofcolumn:).md)
  Returns the rectangle containing the specified column.
- [func rect(ofRow: Int) -> NSRect](ikimagebrowserview/rect(ofrow:).md)
  Returns the rectangle containing the specified row.
- [func rowIndexes(in: NSRect) -> IndexSet!](ikimagebrowserview/rowindexes(in:).md)
  Returns the row indexes in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/columnindexes(in:))*