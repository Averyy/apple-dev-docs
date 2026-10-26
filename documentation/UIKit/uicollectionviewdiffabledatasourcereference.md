# UICollectionViewDiffableDataSourceReference

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

The object you use to manage data and provide cells for a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewDiffableDataSourceReference
```

```objc
@interface UICollectionViewDiffableDataSource : NSObject
```

#### Overview

> ❗ **Important**: If you’re working in a Swift codebase, always use [`UICollectionViewDiffableDataSource`](./uicollectionviewdiffabledatasource-9tqpa.md) instead.

A *diffable data source* object is a specialized type of data source that works together with your collection view object. It provides the behavior you need to manage updates to your collection view’s data and UI in a simple, efficient way. It also conforms to the [`UICollectionViewDataSource`](./uicollectionviewdatasource.md) protocol and provides implementations for all of the protocol’s methods.

To fill a collection view with data:

1. Connect a diffable data source to your collection view.
2. Implement a cell provider to configure your collection view’s cells.
3. Generate the current state of the data.
4. Display the data in the UI.

To connect a diffable data source to a collection view, you create the diffable data source using its [`init(collectionView:cellProvider:)`](./uicollectionviewdiffabledatasourcereference/init%28collectionview,cellprovider%29.md) initializer, passing in the collection view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

```objc
self.dataSource = [[UICollectionViewDiffableDataSource alloc] initWithCollectionView:self.collectionView cellProvider:^UICollectionViewCell *(UICollectionView *collectionView, NSIndexPath *indexPath, id item) {
    // Configure and return cell.
}];
```

Then, you generate the current state of the data and display the data in the UI by constructing and applying a snapshot. For more information, see [`NSDiffableDataSourceSnapshotReference`](./nsdiffabledatasourcesnapshotreference.md).

> ❗ **Important**:  Don’t change the [`dataSource`](./uicollectionview/datasource.md) on the collection view after you configure it with a diffable data source. If the collection view needs a new data source after you configure it initially, create and configure a new collection view and diffable data source.

## Topics

### Creating a diffable data source
- [init(collectionView: UICollectionView, cellProvider: UICollectionViewDiffableDataSourceReferenceCellProvider)](./uicollectionviewdiffabledatasourcereference/init%28collectionview,cellprovider%29.md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.
- [typealias UICollectionViewDiffableDataSourceReferenceCellProvider](./uicollectionviewdiffabledatasourcereferencecellprovider.md)
  A closure that configures and returns a cell for a collection view from its diffable data source.
### Creating supplementary views
- [var supplementaryViewProvider: UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider?](./uicollectionviewdiffabledatasourcereference/supplementaryviewprovider.md)
  The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.
- [typealias UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider](./uicollectionviewdiffabledatasourcereferencesupplementaryviewprovider.md)
  A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.
### Identifying items
- [func itemIdentifier(for: IndexPath) -> Any?](./uicollectionviewdiffabledatasourcereference/itemidentifier%28for%29.md)
  Returns an identifier for the item at the specified index path in the collection view.
- [func indexPath(forItemIdentifier: Any) -> IndexPath?](./uicollectionviewdiffabledatasourcereference/indexpath%28foritemidentifier%29.md)
  Returns an index path for the item with the specified identifier in the collection view.
### Identifying sections
- [func sectionIdentifier(for: Int) -> Any?](./uicollectionviewdiffabledatasourcereference/sectionidentifier%28for%29.md)
  Returns an identifier for the section at the index you specify in the collection view.
- [func index(forSectionIdentifier: Any) -> Int](./uicollectionviewdiffabledatasourcereference/index%28forsectionidentifier%29.md)
  Returns an index for the section with the identifier you specify in the collection view.
### Updating data
- [func snapshot() -> NSDiffableDataSourceSnapshotReference](./uicollectionviewdiffabledatasourcereference/snapshot%28%29.md)
  Returns a representation of the current state of the data in the collection view.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool)](./uicollectionviewdiffabledatasourcereference/applysnapshot%28_,animatingdifferences%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes.
- [func applySnapshot(NSDiffableDataSourceSnapshotReference, animatingDifferences: Bool, completion: (() -> Void)?)](./uicollectionviewdiffabledatasourcereference/applysnapshot%28_,animatingdifferences,completion%29.md)
  Updates the UI to reflect the state of the data in the snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference)](./uicollectionviewdiffabledatasourcereference/applysnapshot%28usingreloaddata%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes.
- [func applySnapshot(usingReloadData: NSDiffableDataSourceSnapshotReference, completion: (() -> Void)?)](./uicollectionviewdiffabledatasourcereference/applysnapshot%28usingreloaddata,completion%29.md)
  Resets the UI to reflect the state of the data in the snapshot without computing a diff or animating the changes, optionally executing a completion handler.
### Updating section data
- [func snapshot(forSection: Any) -> NSDiffableDataSourceSectionSnapshotReference](./uicollectionviewdiffabledatasourcereference/snapshot%28forsection%29.md)
  Returns a representation of the current state of the data in the specified section of the collection view.
- [func applySnapshot(NSDiffableDataSourceSectionSnapshotReference, toSection: Any, animatingDifferences: Bool, completion: (() -> Void)?)](./uicollectionviewdiffabledatasourcereference/applysnapshot%28_,tosection,animatingdifferences,completion%29.md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [func applySnapshot(NSDiffableDataSourceSectionSnapshotReference, toSection: Any, animatingDifferences: Bool)](./uicollectionviewdiffabledatasourcereference/applysnapshot%28_,tosection,animatingdifferences%29.md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.
### Supporting reordering
- [var reorderingHandlers: __UICollectionViewDiffableDataSourceReorderingHandlers](./uicollectionviewdiffabledatasourcereference/reorderinghandlers.md)
  The diffable data source’s handlers for reordering items.
- [UICollectionViewDiffableDataSourceReorderingHandlers](./uicollectionviewdiffabledatasourcereorderinghandlers.md)
  Handlers for reordering items.
- [NSDiffableDataSourceTransaction](./nsdiffabledatasourcetransaction-c.class.md)
  A transaction that describes the changes after reordering the items in the view.
- [NSDiffableDataSourceSectionTransaction](./nsdiffabledatasourcesectiontransaction-c.class.md)
  A transaction that describes the changes after reordering the items in a section.
### Supporting expanding and collapsing
- [var sectionSnapshotHandlers: __UICollectionViewDiffableDataSourceSectionSnapshotHandlers](./uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers.md)
  The diffable data source’s handlers for expanding and collapsing items.
- [UICollectionViewDiffableDataSourceSectionSnapshotHandlers](./uicollectionviewdiffabledatasourcesectionsnapshothandlers.md)
  Handlers for expanding and collapsing items.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UICollectionViewDataSource](./uicollectionviewdatasource.md)

## See Also

### Data
- [Updating collection views using diffable data sources](./updating-collection-views-using-diffable-data-sources.md)
  Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](./implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [Building high-performance lists and collection views](./building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
- [UICollectionViewDataSource](./uicollectionviewdatasource.md)
  The methods adopted by the object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSourcePrefetching](./uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
- [NSDiffableDataSourceSnapshot](./nsdiffabledatasourcesnapshotreference.md)
  A representation of the state of the data in a view at a specific point in time.
- [NSDiffableDataSourceSectionSnapshot](./nsdiffabledatasourcesectionsnapshotreference.md)
  A representation of the state of the data in a layout section at a specific point in time.
- [UIRefreshControl](./uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference)*