# rowIndexes(in:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the row indexes in the specified rectangle.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func rowIndexes(in rect: NSRect) -> IndexSet!
```

```objc
- (NSIndexSet *) rowIndexesInRect:(NSRect) rect;
```

#### Return Value

An index set containing the item indexes.

## Parameters

- `rect`: A rectangle in the view’s coordinate system.

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
- [func rect(ofRow: Int) -> NSRect](./rect%28ofrow%29.md)
  Returns the rectangle containing the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/rowindexes(in:))*