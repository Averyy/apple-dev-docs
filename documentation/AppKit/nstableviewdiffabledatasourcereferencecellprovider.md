# NSTableViewDiffableDataSourceReferenceCellProvider

**Framework**: AppKit  
**Kind**: typealias

A closure that configures and returns a cell for a table view from its diffable data source.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias NSTableViewDiffableDataSourceReferenceCellProvider = (NSTableView, NSTableColumn, Int, Any) -> NSView
```

## See Also

- [init(tableView: NSTableView, cellProvider: NSTableViewDiffableDataSourceReferenceCellProvider)](nstableviewdiffabledatasourcereference/init(tableview:cellprovider:).md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereferencecellprovider)*