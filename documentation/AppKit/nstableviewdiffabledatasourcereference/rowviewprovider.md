# rowViewProvider

**Framework**: AppKit  
**Kind**: property

The closure that configures and returns the table view’s row views from the diffable data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var rowViewProvider: NSTableViewDiffableDataSourceReferenceRowProvider? { get set }
```

#### Discussion

This property replaces the [`tableView(_:rowViewForRow:)`](nstableviewdelegate/tableview(_:rowviewforrow:).md) delegate method.

## See Also

- [var sectionHeaderViewProvider: NSTableViewDiffableDataSourceReferenceSectionHeaderViewProvider?](nstableviewdiffabledatasourcereference/sectionheaderviewprovider.md)
  The closure that configures and returns the table view’s section header views from the diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceRowProvider](nstableviewdiffabledatasourcereferencerowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceSectionHeaderViewProvider](nstableviewdiffabledatasourcereferencesectionheaderviewprovider.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasourcereference/rowviewprovider)*