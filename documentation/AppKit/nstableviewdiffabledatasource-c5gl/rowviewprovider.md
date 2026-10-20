# rowViewProvider

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The closure that configures and returns the table view’s row views from the diffable data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var rowViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.RowProvider?
```

#### Discussion

This property replaces the [`tableView(_:rowViewForRow:)`](../nstableviewdelegate/tableview%28_,rowviewforrow%29.md) delegate method.

## See Also

### Creating Row and Section Views
- [var sectionHeaderViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionHeaderViewProvider?](./sectionheaderviewprovider-swift.property.md)
  The closure that configures and returns the table view’s section header views from the diffable data source.
- [NSTableViewDiffableDataSource.RowProvider](./rowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceRowProvider](../nstableviewdiffabledatasourcereferencerowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [NSTableViewDiffableDataSource.SectionHeaderViewProvider](./sectionheaderviewprovider-swift.typealias.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceSectionHeaderViewProvider](../nstableviewdiffabledatasourcereferencesectionheaderviewprovider.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/rowviewprovider)*