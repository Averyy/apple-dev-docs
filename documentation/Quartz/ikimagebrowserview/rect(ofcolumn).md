# rect(ofColumn:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle containing the specified column.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func rect(ofColumn columnIndex: Int) -> NSRect
```

```objc
- (NSRect) rectOfColumn:(NSUInteger) columnIndex;
```

#### Return Value

A rectangle containing the column. Specified in the view’s coordinate system.

## Parameters

- `columnIndex`: The column index.

## See Also

### Getting Columns and Rows Information
- [func numberOfColumns() -> Int](./numberofcolumns%28%29.md)
  Returns the current number of columns.
- [func numberOfRows() -> Int](./numberofrows%28%29.md)
  Returns the current number of rows.
- [func columnIndexes(in: NSRect) -> IndexSet!](./columnindexes%28in%29.md)
  Returns the column indexes in the specified rectangle.
- [func rect(ofRow: Int) -> NSRect](./rect%28ofrow%29.md)
  Returns the rectangle containing the specified row.
- [func rowIndexes(in: NSRect) -> IndexSet!](./rowindexes%28in%29.md)
  Returns the row indexes in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/rect(ofcolumn:))*