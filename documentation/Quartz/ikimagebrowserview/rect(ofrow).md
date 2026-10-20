# rect(ofRow:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle containing the specified row.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func rect(ofRow rowIndex: Int) -> NSRect
```

```objc
- (NSRect) rectOfRow:(NSUInteger) rowIndex;
```

#### Return Value

A rectangle containing the column. Specified in the view’s coordinate system.

## Parameters

- `rowIndex`: The row index.

## See Also

### Getting Columns and Rows Information
- [func numberOfColumns() -> Int](./numberofcolumns%28%29.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](./numberofrows%28%29.md)
  Returns the current number of rows.
- [func rect(ofColumn: Int) -> NSRect](./rect%28ofcolumn%29.md)
  Returns the rectangle containing the specified column.
- [func columnIndexes(in: NSRect) -> IndexSet!](./columnindexes%28in%29.md)
  Returns the column indexes in the specified rectangle.
- [func rowIndexes(in: NSRect) -> IndexSet!](./rowindexes%28in%29.md)
  Returns the row indexes in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/rect(ofrow:))*