# dataSource

**Framework**: AppKit  
**Kind**: property

The object that provides the data displayed by the table view.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var dataSource: (any NSTableViewDataSource)? { get set }
```

#### Discussion

The data source for the table view must implement the appropriate methods of the [`NSTableViewDataSource`](nstableviewdatasource.md) protocol. For more information, see the [`NSTableViewDataSource`](nstableviewdatasource.md) `protocol` specification. Note that in versions of macOS prior to v10.12, the table view did not retain the data source in a managed memory environment.

Setting the data source invokes [`tile()`](nstableview/tile().md).

If the delegate doesn’t respond to either [`numberOfRows(in:)`](nstableviewdatasource/numberofrows(in:).md) or [`tableView(_:objectValueFor:row:)`](nstableviewdatasource/tableview(_:objectvaluefor:row:).md), [`internalInconsistencyException`](https://developer.apple.com/documentation/foundation/nsexceptionname/internalinconsistencyexception) may be raised.

## See Also

- [var usesStaticContents: Bool](nstableview/usesstaticcontents.md)
  A Boolean value indicating whether the table uses static data.
- [func reloadData()](nstableview/reloaddata.md)
  Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.
- [func reloadData(forRowIndexes: IndexSet, columnIndexes: IndexSet)](nstableview/reloaddata(forrowindexes:columnindexes:).md)
  Reloads the data for only the specified rows and columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/datasource)*