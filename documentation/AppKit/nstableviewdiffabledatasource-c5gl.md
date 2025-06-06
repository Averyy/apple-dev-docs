# NSTableViewDiffableDataSource

**Framework**: AppKit  
**Kind**: class

The object you use to manage data and provide items for a table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, ItemIdentifierType : Hashable
```

#### Overview

A  object is a specialized type of data source that works together with your table view object. It provides the behavior you need to manage updates to your table view’s data and UI in a simple, efficient way. It also conforms to the [`NSTableViewDataSource`](nstableviewdatasource.md) protocol.

To fill a table view with data:

1. Connect a diffable data source to your table view.
2. Implement a cell provider to configure your table view’s cells.
3. Generate the current state of the data.
4. Display the data in the UI.

To connect a diffable data source to a table view, you create the diffable data source using its [`init(tableView:cellProvider:)`](nstableviewdiffabledatasource-c5gl/init(tableview:cellprovider:).md) initializer, passing in the table view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

Then, you generate the current state of the data and display the data in the UI by constructing and applying a snapshot. For more information, see [`NSDiffableDataSourceSnapshot`](nsdiffabledatasourcesnapshot-swift.struct.md).

## Topics

### Creating a Diffable Data Source
- [init(tableView: NSTableView, cellProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)](nstableviewdiffabledatasource-c5gl/init(tableview:cellprovider:).md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified table view.
- [NSTableViewDiffableDataSource.CellProvider](nstableviewdiffabledatasource-c5gl/cellprovider.md)
  A closure that configures and returns a cell for a table view from its diffable data source.
### Creating Row and Section Views
- [var rowViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.RowProvider?](nstableviewdiffabledatasource-c5gl/rowviewprovider.md)
  The closure that configures and returns the table view’s row views from the diffable data source.
- [var sectionHeaderViewProvider: NSTableViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionHeaderViewProvider?](nstableviewdiffabledatasource-c5gl/sectionheaderviewprovider-swift.property.md)
  The closure that configures and returns the table view’s section header views from the diffable data source.
- [NSTableViewDiffableDataSource.RowProvider](nstableviewdiffabledatasource-c5gl/rowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceRowProvider](nstableviewdiffabledatasourcereferencerowprovider.md)
  A closure that configures and returns a row view for a table view from its diffable data source.
- [NSTableViewDiffableDataSource.SectionHeaderViewProvider](nstableviewdiffabledatasource-c5gl/sectionheaderviewprovider-swift.typealias.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.
- [typealias NSTableViewDiffableDataSourceReferenceSectionHeaderViewProvider](nstableviewdiffabledatasourcereferencesectionheaderviewprovider.md)
  A closure that configures and returns a section header view for a table view from its diffable data source.
### Identifying Items and Sections
- [func itemIdentifier(forRow: Int) -> ItemIdentifierType?](nstableviewdiffabledatasource-c5gl/itemidentifier(forrow:).md)
  Returns an identifier for the item at the specified row in the table view.
- [func row(forItemIdentifier: ItemIdentifierType) -> Int?](nstableviewdiffabledatasource-c5gl/row(foritemidentifier:).md)
  Returns a row for the item with the specified identifier in the table view.
- [func sectionIdentifier(forRow: Int) -> SectionIdentifierType?](nstableviewdiffabledatasource-c5gl/sectionidentifier(forrow:).md)
  Returns the identifier of the section containing the specified row in the snapshot.
- [func row(forSectionIdentifier: SectionIdentifierType) -> Int?](nstableviewdiffabledatasource-c5gl/row(forsectionidentifier:).md)
  Returns a row for the section with the specified identifier in the table view.
### Updating Data
- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nstableviewdiffabledatasource-c5gl/snapshot.md)
  Returns a representation of the current state of the data in the table view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](nstableviewdiffabledatasource-c5gl/apply(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [var defaultRowAnimation: NSTableView.AnimationOptions](nstableviewdiffabledatasource-c5gl/defaultrowanimation.md)
  The default animation the UI uses to show differences between rows.
### Supporting Bridging
- [class NSTableViewDiffableDataSourceReference](nstableviewdiffabledatasourcereference.md)
  The object you use to manage data and provide items for a table view.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTableViewDataSource](nstableviewdatasource.md)

## See Also

- [protocol NSTableViewDataSource](nstableviewdatasource.md)
  A set of methods that a table view uses to provide data to a table view and to allow the editing of the table view’s data source object.
- [protocol NSTableViewDelegate](nstableviewdelegate.md)
  A set of optional methods you implement in a table view delegate to customize the behavior of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdiffabledatasource-c5gl)*