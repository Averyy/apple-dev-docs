# index(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the specified grid row.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func index(of row: NSGridRow) -> Int
```

```objc
- (NSInteger) indexOfRow:(NSGridRow *) row;
```

## See Also

### Getting Information About the Grid
- [var numberOfRows: Int](./numberofrows.md)
  The number of rows in the grid view.
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns in the grid view.
- [func index(of: NSGridColumn) -> Int](./index%28of%29-32sdd.md)
  Returns the index of the specified grid column.
- [func row(at: Int) -> NSGridRow](./row%28at%29.md)
  Returns the grid row object at the specified index.
- [func column(at: Int) -> NSGridColumn](./column%28at%29.md)
  Returns the grid column object at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/index(of:)-6zs2o)*