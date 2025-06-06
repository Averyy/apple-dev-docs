# NSTableViewDiffableDataSource.SectionHeaderViewProvider

**Framework**: AppKit  
**Kind**: typealias

A closure that configures and returns a section header view for a table view from its diffable data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
typealias SectionHeaderViewProvider = (NSTableView, Int, SectionIdentifierType) -> NSView
```

## See Also

- [var rowViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.RowProvider?](nstableviewdiffabledatasource-c5gl/rowviewprovider.md)
  The closure that configures and returns the table view’s row views from the diffable data source.
- [var sectionHeaderViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionHeaderViewProvider?](nstableviewdiffabledatasource-c5gl/sectionheaderviewprovider-swift.property.md)
  The closure that configures and returns the table view’s section header views from the diffable data source.
- [NSTableViewDiffableDataSource.RowProvider](nstableviewdiffabledatasource-c5gl/rowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceRowProvider](nstableviewdiffabledatasourcereferencerowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceSectionHeaderViewProvider](nstableviewdiffabledatasourcereferencesectionheaderviewprovider.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl/sectionheaderviewprovider-swift.typealias)*