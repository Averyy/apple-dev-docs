# dataSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that provides the data displayed by the table view.

**Availability**:
- macOS

## Declaration

```swift
weak var dataSource: (any NSTableViewDataSource)? { get set }
```

```objc
@property (weak, nullable) id<NSTableViewDataSource> dataSource;
```

## Discussion

The data source for the table view must implement the appropriate methods of the [`NSTableViewDataSource`](../nstableviewdatasource.md) protocol. For more information, see the [`NSTableViewDataSource`](../nstableviewdatasource.md) `protocol` specification. Note that in versions of macOS prior to v10.12, the table view did not retain the data source in a managed memory environment.

Setting the data source invokes [`tile()`](./tile%28%29.md).

If the delegate doesn’t respond to either [`numberOfRows(in:)`](../nstableviewdatasource/numberofrows%28in%29.md) or [`tableView(_:objectValueFor:row:)`](../nstableviewdatasource/tableview%28_,objectvaluefor,row%29.md), [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) may be raised.

## See Also

### Managing the Table’s Data
- [var usesStaticContents: Bool](./usesstaticcontents.md)
  A Boolean value indicating whether the table uses static data.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.
- [func reloadData(forRowIndexes: IndexSet, columnIndexes: IndexSet)](./reloaddata%28forrowindexes,columnindexes%29.md)
  Reloads the data for only the specified rows and columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/datasource)*