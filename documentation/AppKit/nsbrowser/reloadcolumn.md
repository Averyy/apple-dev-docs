# reloadColumn(_:)

**Framework**: AppKit  
**Kind**: method

Reloads the given column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reloadColumn(_ column: Int)
```

#### Discussion

If after reloading the selected item no longer exists in the column, the column is set to be the last column.

## Parameters

- `column`: The index of the column to reload.

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
- [func validateVisibleColumns()](nsbrowser/validatevisiblecolumns.md)
  Validates the browser’s visible columns.
- [var isLoaded: Bool](nsbrowser/isloaded.md)
  A Boolean that indicates whether column 0 is loaded.
- [func loadColumnZero()](nsbrowser/loadcolumnzero.md)
  Loads column 0; unloads previously loaded columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/reloadcolumn(_:))*