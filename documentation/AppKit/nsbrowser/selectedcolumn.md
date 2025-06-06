# selectedColumn

**Framework**: AppKit  
**Kind**: property

The index of the last column with a selected item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedColumn: Int { get }
```

#### Discussion

When the value of this property is `-1`, there is no column selected.

## See Also

- [func selectAll(Any?)](nsbrowser/selectall(_:).md)
  Selects all cells in the last column of the browser.
- [func column(of: NSMatrix) -> Int](nsbrowser/column(of:).md)
  Returns the column number in which the given matrix is located.
- [func addColumn()](nsbrowser/addcolumn.md)
  Adds a column to the right of the last column.
- [var lastColumn: Int](nsbrowser/lastcolumn.md)
  The index of the last column loaded.
- [var firstVisibleColumn: Int](nsbrowser/firstvisiblecolumn.md)
  The index of the first visible column.
- [var numberOfVisibleColumns: Int](nsbrowser/numberofvisiblecolumns.md)
  The number of visible columns.
- [var lastVisibleColumn: Int](nsbrowser/lastvisiblecolumn.md)
  The index of the last visible column.
- [func validateVisibleColumns()](nsbrowser/validatevisiblecolumns.md)
  Validates the browser’s visible columns.
- [var isLoaded: Bool](nsbrowser/isloaded.md)
  A Boolean that indicates whether column 0 is loaded.
- [func loadColumnZero()](nsbrowser/loadcolumnzero.md)
  Loads column 0; unloads previously loaded columns.
- [func reloadColumn(Int)](nsbrowser/reloadcolumn(_:).md)
  Reloads the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectedcolumn)*