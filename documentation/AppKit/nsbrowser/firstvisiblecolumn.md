# firstVisibleColumn

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the first visible column.

**Availability**:
- macOS

## Declaration

```swift
var firstVisibleColumn: Int { get }
```

```objc
@property (readonly) NSInteger firstVisibleColumn;
```

## See Also

### Managing Columns
- [func addColumn()](./addcolumn%28%29.md)
  Adds a column to the right of the last column.
- [var selectedColumn: Int](./selectedcolumn.md)
  The index of the last column with a selected item.
- [var lastColumn: Int](./lastcolumn.md)
  The index of the last column loaded.
- [var numberOfVisibleColumns: Int](./numberofvisiblecolumns.md)
  The number of visible columns.
- [var lastVisibleColumn: Int](./lastvisiblecolumn.md)
  The index of the last visible column.
- [func validateVisibleColumns()](./validatevisiblecolumns%28%29.md)
  Validates the browser’s visible columns.
- [var isLoaded: Bool](./isloaded.md)
  A Boolean that indicates whether column 0 is loaded.
- [func loadColumnZero()](./loadcolumnzero%28%29.md)
  Loads column 0; unloads previously loaded columns.
- [func reloadColumn(Int)](./reloadcolumn%28_%29.md)
  Reloads the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/firstvisiblecolumn)*