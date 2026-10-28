# sectionHeaderViewProvider

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The closure that configures and returns the table view’s section header views from the diffable data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var sectionHeaderViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionHeaderViewProvider?
```

## Discussion

This property replaces the [`tableView(_:viewFor:row:)`](../nstableviewdelegate/tableview%28_,viewfor,row%29.md) method for group rows when the `tableColumn` parameter in [`tableView(_:viewFor:row:)`](../nstableviewdelegate/tableview%28_,viewfor,row%29.md) would be `nil`. Setting this property means the table view never invokes its delegate’s [`tableView(_:isGroupRow:)`](../nstableviewdelegate/tableview%28_,isgrouprow%29.md) method. Instead, it uses the current snapshot’s sections.

## See Also

### Creating Row and Section Views
- [var rowViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.RowProvider?](./rowviewprovider.md)
  The closure that configures and returns the table view’s row views from the diffable data source.
- [NSTableViewDiffableDataSource.RowProvider](./rowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceRowProvider](../nstableviewdiffabledatasourcereferencerowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [NSTableViewDiffableDataSource.SectionHeaderViewProvider](./sectionheaderviewprovider-swift.typealias.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceSectionHeaderViewProvider](../nstableviewdiffabledatasourcereferencesectionheaderviewprovider.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/sectionheaderviewprovider-swift.property)*