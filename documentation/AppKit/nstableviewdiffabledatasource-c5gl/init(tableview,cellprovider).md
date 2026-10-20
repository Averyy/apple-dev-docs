# init(tableView:cellProvider:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a diffable data source with the specified cell provider, and connects it to the specified table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(tableView: NSTableView, cellProvider: @escaping NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)
```

## Parameters

- `tableView`: The initialized table view object to connect to the diffable data source.
- `cellProvider`: A closure that creates and returns each of the cells for the table view from the data the diffable data source provides. This replaces the [`tableView(_:viewFor:row:)`](../nstableviewdelegate/tableview%28_,viewfor,row%29.md) delegate method.

## See Also

### Creating a Diffable Data Source
- [NSTableViewDiffableDataSource.CellProvider](./cellprovider.md)
  A closure that configures and returns a cell for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/init(tableview:cellprovider:))*