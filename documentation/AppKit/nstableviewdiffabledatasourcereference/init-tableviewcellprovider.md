# init(tableView:cellProvider:)

**Framework**: AppKit  
**Kind**: init

Creates a diffable data source with the specified cell provider, and connects it to the specified table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(tableView: NSTableView, cellProvider: @escaping NSTableViewDiffableDataSourceReferenceCellProvider)
```

## Parameters

- `tableView`: The initialized table view object to connect to the diffable data source.
- `cellProvider`: A closure that creates and returns each of the cells for the table view from the data the diffable data source provides. This replaces the   delegate method.

## See Also

- [typealias NSTableViewDiffableDataSourceReferenceCellProvider](nstableviewdiffabledatasourcereferencecellprovider.md)
  A closure that configures and returns a cell for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/init(tableview:cellprovider:))*