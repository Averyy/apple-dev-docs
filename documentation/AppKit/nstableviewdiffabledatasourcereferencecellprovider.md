# NSTableViewDiffableDataSourceReferenceCellProvider

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that configures and returns a cell for a table view from its diffable data source.

**Availability**:
- macOS

## Declaration

```swift
typealias NSTableViewDiffableDataSourceReferenceCellProvider = (NSTableView, NSTableColumn, Int, Any) -> NSView
```

```c
typedef NSView *(^)(NSTableView *, NSTableColumn *, long, id) NSTableViewDiffableDataSourceCellProvider;
```

## See Also

### Creating a Diffable Data Source
- [init(tableView: NSTableView, cellProvider: NSTableViewDiffableDataSourceReferenceCellProvider)](./nstableviewdiffabledatasourcereference/init%28tableview,cellprovider%29.md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereferencecellprovider)*