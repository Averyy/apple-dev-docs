# columnIndexes(in:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the column indexes in the specified rectangle.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func columnIndexes(in rect: NSRect) -> IndexSet!
```

```objc
- (NSIndexSet *) columnIndexesInRect:(NSRect) rect;
```

#### Return Value

An index set containing the cell indexes.

## Parameters

- `rect`: The rectangle in the view’s coordinate system.

## See Also

### Getting Columns and Rows Information
- [func numberOfColumns() -> Int](./numberofcolumns%28%29.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](./numberofrows%28%29.md)
  Returns the current number of rows.
- [func rect(ofColumn: Int) -> NSRect](./rect%28ofcolumn%29.md)
  Returns the rectangle containing the specified column.
- [func rect(ofRow: Int) -> NSRect](./rect%28ofrow%29.md)
  Returns the rectangle containing the specified row.
- [func rowIndexes(in: NSRect) -> IndexSet!](./rowindexes%28in%29.md)
  Returns the row indexes in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/columnindexes(in:))*