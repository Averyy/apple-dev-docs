# numberOfRows()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the current number of rows.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func numberOfRows() -> Int
```

```objc
- (NSUInteger) numberOfRows;
```

## Return Value

The number of rows.

## See Also

### Getting Columns and Rows Information
- [func numberOfColumns() -> Int](./numberofcolumns%28%29.md)
  Returns the current number of columns.
- [func rect(ofColumn: Int) -> NSRect](./rect%28ofcolumn%29.md)
  Returns the rectangle containing the specified column.
- [func columnIndexes(in: NSRect) -> IndexSet!](./columnindexes%28in%29.md)
  Returns the column indexes in the specified rectangle.
- [func rect(ofRow: Int) -> NSRect](./rect%28ofrow%29.md)
  Returns the rectangle containing the specified row.
- [func rowIndexes(in: NSRect) -> IndexSet!](./rowindexes%28in%29.md)
  Returns the row indexes in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/numberofrows())*