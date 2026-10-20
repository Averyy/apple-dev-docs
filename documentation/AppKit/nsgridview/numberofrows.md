# numberOfRows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of rows in the grid view.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var numberOfRows: Int { get }
```

```objc
@property (readonly) NSInteger numberOfRows;
```

## See Also

### Getting Information About the Grid
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns in the grid view.
- [func index(of: NSGridColumn) -> Int](./index%28of%29-32sdd.md)
  Returns the index of the specified grid column.
- [func row(at: Int) -> NSGridRow](./row%28at%29.md)
  Returns the grid row object at the specified index.
- [func column(at: Int) -> NSGridColumn](./column%28at%29.md)
  Returns the grid column object at the specified index.
- [func index(of: NSGridRow) -> Int](./index%28of%29-6zs2o.md)
  Returns the index of the specified grid row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/numberofrows)*