# UICollectionViewDiffableDataSource

**Framework**: UIKit  
**Kind**: class

The object you use to manage data and provide cells for a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

#### Overview

A  object is a specialized type of data source that works together with your collection view object. It provides the behavior you need to manage updates to your collection view’s data and UI in a simple, efficient way. It also conforms to the [`UICollectionViewDataSource`](uicollectionviewdatasource.md) protocol and provides implementations for all of the protocol’s methods.

To fill a collection view with data:

1. Connect a diffable data source to your collection view.
2. Implement a cell provider to configure your collection view’s cells.
3. Generate the current state of the data.
4. Display the data in the UI.

To connect a diffable data source to a collection view, you create the diffable data source using its [`init(collectionView:cellProvider:)`](uicollectionviewdiffabledatasource-9tqpa/init(collectionview:cellprovider:).md) initializer, passing in the collection view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

```swift
dataSource = UICollectionViewDiffableDataSource<Int, UUID>(collectionView: collectionView) {
    (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: UUID) -> UICollectionViewCell? in
    // Configure and return cell.
}
```

Then, you generate the current state of the data and display the data in the UI by constructing and applying a snapshot. For more information, see [`NSDiffableDataSourceSnapshot`](nsdiffabledatasourcesnapshot-swift.struct.md).

> ❗ **Important**:  Don’t change the [`dataSource`](uitableview/datasource.md) on the collection view after you configure it with a diffable data source. If the collection view needs a new data source after you configure it initially, create and configure a new collection view and diffable data source.

## Topics

### Creating a diffable data source
- [init(collectionView: UICollectionView, cellProvider: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)](uicollectionviewdiffabledatasource-9tqpa/init(collectionview:cellprovider:).md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.
- [UICollectionViewDiffableDataSource.CellProvider](uicollectionviewdiffabledatasource-9tqpa/cellprovider.md)
  A closure that configures and returns a cell for a collection view from its diffable data source.
### Creating supplementary views
- [var supplementaryViewProvider: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SupplementaryViewProvider?](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property.md)
  The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.
- [UICollectionViewDiffableDataSource.SupplementaryViewProvider](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias.md)
  A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.
### Identifying items
- [func itemIdentifier(for: IndexPath) -> ItemIdentifierType?](uicollectionviewdiffabledatasource-9tqpa/itemidentifier(for:).md)
  Returns an identifier for the item at the specified index path in the collection view.
- [func indexPath(for: ItemIdentifierType) -> IndexPath?](uicollectionviewdiffabledatasource-9tqpa/indexpath(for:).md)
  Returns an index path for the item with the specified identifier in the collection view.
### Identifying sections
- [func sectionIdentifier(for: Int) -> SectionIdentifierType?](uicollectionviewdiffabledatasource-9tqpa/sectionidentifier(for:).md)
  Returns an identifier for the section at the index you specify in the collection view.
- [func index(for: SectionIdentifierType) -> Int?](uicollectionviewdiffabledatasource-9tqpa/index(for:).md)
  Returns an index for the section with the identifier you specify in the collection view.
### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](uicollectionviewdiffabledatasource-9tqpa/snapshot.md)
  Returns a representation of the current state of the data in the collection view.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool) async](uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](uicollectionviewdiffabledatasource-9tqpa/apply(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>) async](uicollectionviewdiffabledatasource-9tqpa/applysnapshotusingreloaddata(_:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshotUsingReloadData(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, completion: (() -> Void)?)](uicollectionviewdiffabledatasource-9tqpa/applysnapshotusingreloaddata(_:completion:).md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
### Updating section data
- [func snapshot(for: SectionIdentifierType) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](uicollectionviewdiffabledatasource-9tqpa/snapshot(for:).md)
  Returns a representation of the current state of the data in the specified section of the collection view.
- [func apply(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to: SectionIdentifierType, animatingDifferences: Bool, completion: (() -> Void)?)](uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:completion:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [func apply(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to: SectionIdentifierType, animatingDifferences: Bool) async](uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.
### Supporting reordering
- [var reorderingHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property.md)
  The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSource.ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct.md)
  Handlers for reordering items.
- [struct NSDiffableDataSourceTransaction](nsdiffabledatasourcetransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in the view.
- [struct NSDiffableDataSourceSectionTransaction](nsdiffabledatasourcesectiontransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in a section.
### Supporting expanding and collapsing
- [var sectionSnapshotHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionSnapshotHandlers<ItemIdentifierType>](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.property.md)
  The diffable data source’s handlers for expanding and collapsing items.
- [UICollectionViewDiffableDataSource.SectionSnapshotHandlers](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct.md)
  Handlers for expanding and collapsing items.
### Debugging a diffable data source
- [func description() -> String](uicollectionviewdiffabledatasource-9tqpa/description.md)
  Returns a string with a description of the diffable data source.
### Supporting bridging
- [class UICollectionViewDiffableDataSourceReference](uicollectionviewdiffabledatasourcereference.md)
  The object you use to manage data and provide cells for a collection view.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UICollectionViewDataSource](uicollectionviewdatasource.md)

## See Also

- [Updating collection views using diffable data sources](updating-collection-views-using-diffable-data-sources.md)
  Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
- [protocol UICollectionViewDataSource](uicollectionviewdatasource.md)
  The methods adopted by the object you use to manage data and provide cells for a collection view.
- [protocol UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.
- [struct NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md)
  A representation of the state of the data in a layout section at a specific point in time.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa)*