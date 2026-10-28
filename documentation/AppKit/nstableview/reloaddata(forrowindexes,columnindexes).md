# reloadData(forRowIndexes:columnIndexes:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reloads the data for only the specified rows and columns.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func reloadData(forRowIndexes rowIndexes: IndexSet, columnIndexes: IndexSet)
```

```objc
- (void) reloadDataForRowIndexes:(NSIndexSet *) rowIndexes columnIndexes:(NSIndexSet *) columnIndexes;
```

## Discussion

For cells that are visible, the appropriate [`dataSource`](./datasource.md) and [`delegate`](./delegate.md) methods are called and the cells are redrawn.

For tables that support variable row heights, the row height is not re-queried from the delegate; it is your responsibility to invoke [`noteHeightOfRows(withIndexesChanged:)`](./noteheightofrows%28withindexeschanged%29.md) if a row height change is required.

> **Note**:  For [`NSView`](../nsview.md)-based table views, this method drops the view-cells in the table row, but not the [`NSTableRowView`](../nstablerowview.md) instances.

## Parameters

- `rowIndexes`: The indexes of the rows to update.
- `columnIndexes`: The indexes of the columns to update.

## See Also

### Managing the Table’s Data
- [var dataSource: (any NSTableViewDataSource)?](./datasource.md)
  The object that provides the data displayed by the table view.
- [var usesStaticContents: Bool](./usesstaticcontents.md)
  A Boolean value indicating whether the table uses static data.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/reloaddata(forrowindexes:columnindexes:))*