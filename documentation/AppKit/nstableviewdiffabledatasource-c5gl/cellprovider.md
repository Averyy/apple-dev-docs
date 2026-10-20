# NSTableViewDiffableDataSource.CellProvider

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that configures and returns a cell for a table view from its diffable data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
typealias CellProvider = (NSTableView, NSTableColumn, Int, ItemIdentifierType) -> NSView
```

## See Also

### Creating a Diffable Data Source
- [init(tableView: NSTableView, cellProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)](./init%28tableview,cellprovider%29.md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/cellprovider)*