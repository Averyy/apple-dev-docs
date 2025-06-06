# reloadData(forRowIndexes:columnIndexes:)

**Framework**: Appkit  
**Kind**: method

Reloads the data for only the specified rows and columns.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func reloadData(forRowIndexes rowIndexes: IndexSet, columnIndexes: IndexSet)
```

#### Discussion

For cells that are visible, the appropriate [`dataSource`](nstableview/datasource.md) and [`delegate`](nstableview/delegate.md) methods are called and the cells are redrawn.

For tables that support variable row heights, the row height is not re-queried from the delegate; it is your responsibility to invoke [`noteHeightOfRows(withIndexesChanged:)`](nstableview/noteheightofrows(withindexeschanged:).md) if a row height change is required.

> **Note**:  For [`NSView`](nsview.md)-based table views, this method drops the view-cells in the table row, but not the [`NSTableRowView`](nstablerowview.md) instances.

## Parameters

- `rowIndexes`: The indexes of the rows to update.
- `columnIndexes`: The indexes of the columns to update.

## See Also

- [var dataSource: (any NSTableViewDataSource)?](nstableview/datasource.md)
  The object that provides the data displayed by the table view.
- [var usesStaticContents: Bool](nstableview/usesstaticcontents.md)
  A Boolean value indicating whether the table uses static data.
- [func reloadData()](nstableview/reloaddata.md)
  Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/reloaddata(forrowindexes:columnindexes:))*