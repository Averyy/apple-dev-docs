# validateVisibleColumns()

**Framework**: AppKit  
**Kind**: method

Validates the browser’s visible columns.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateVisibleColumns()
```

#### Discussion

This method invokes the delegate method [`browser(_:isColumnValid:)`](nsbrowserdelegate/browser(_:iscolumnvalid:).md)

## See Also

- [func addColumn()](nsbrowser/addcolumn.md)
  Adds a column to the right of the last column.
- [var selectedColumn: Int](nsbrowser/selectedcolumn.md)
  The index of the last column with a selected item.
- [var lastColumn: Int](nsbrowser/lastcolumn.md)
  The index of the last column loaded.
- [var firstVisibleColumn: Int](nsbrowser/firstvisiblecolumn.md)
  The index of the first visible column.
- [var numberOfVisibleColumns: Int](nsbrowser/numberofvisiblecolumns.md)
  The number of visible columns.
- [var lastVisibleColumn: Int](nsbrowser/lastvisiblecolumn.md)
  The index of the last visible column.
- [var isLoaded: Bool](nsbrowser/isloaded.md)
  A Boolean that indicates whether column 0 is loaded.
- [func loadColumnZero()](nsbrowser/loadcolumnzero.md)
  Loads column 0; unloads previously loaded columns.
- [func reloadColumn(Int)](nsbrowser/reloadcolumn(_:).md)
  Reloads the given column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/validatevisiblecolumns())*