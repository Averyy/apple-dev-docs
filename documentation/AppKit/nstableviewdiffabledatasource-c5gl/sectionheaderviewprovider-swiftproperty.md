# sectionHeaderViewProvider

**Framework**: AppKit  
**Kind**: property

The closure that configures and returns the table view’s section header views from the diffable data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var sectionHeaderViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionHeaderViewProvider?
```

#### Discussion

This property replaces the [`tableView(_:viewFor:row:)`](nstableviewdelegate/tableview(_:viewfor:row:).md) method for group rows when the `tableColumn` parameter in [`tableView(_:viewFor:row:)`](nstableviewdelegate/tableview(_:viewfor:row:).md) would be `nil`. Setting this property means the table view never invokes its delegate’s [`tableView(_:isGroupRow:)`](nstableviewdelegate/tableview(_:isgrouprow:).md) method. Instead, it uses the current snapshot’s sections.

## See Also

- [var rowViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.RowProvider?](nstableviewdiffabledatasource-c5gl/rowviewprovider.md)
  The closure that configures and returns the table view’s row views from the diffable data source.
- [NSTableViewDiffableDataSource.RowProvider](nstableviewdiffabledatasource-c5gl/rowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceRowProvider](nstableviewdiffabledatasourcereferencerowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [NSTableViewDiffableDataSource.SectionHeaderViewProvider](nstableviewdiffabledatasource-c5gl/sectionheaderviewprovider-swift.typealias.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceSectionHeaderViewProvider](nstableviewdiffabledatasourcereferencesectionheaderviewprovider.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/sectionheaderviewprovider-swift.property)*