# NSDiffableDataSourceSnapshot

**Framework**: UIKit  
**Kind**: struct

A representation of the state of the data in a view at a specific point in time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
struct NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType> where SectionIdentifierType : Hashable, SectionIdentifierType : Sendable, ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

#### Overview

Diffable data sources use  to provide data for collection views and table views. You use a snapshot to set up the initial state of the data that a view displays, and you use snapshots to reflect changes to the data that the view displays.

The data in a snapshot is made up of the sections and items you want to display, in the order you that you determine. You configure what to display by adding, deleting, or moving the sections and items.

> ❗ **Important**:  Each of your sections and items must have unique identifiers that conform to the [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) protocol. Use `struct` or `enum` Swift value types for your identifiers, including built-in types such as `Int`, `String`, or `UUID`. If you use a Swift `class` for your identifiers, your `class` must be a subclass of `NSObject`.

To display data in a view using a snapshot:

1. Create a snapshot and populate it with the state of the data you want to display.
2. Apply the snapshot to reflect the changes in the UI.

You can create and configure a snapshot in one of these ways:

- Create an empty snapshot, then append sections and items to it.
- Get the current snapshot by calling the diffable data source’s [`snapshot()`](uicollectionviewdiffabledatasource-9tqpa/snapshot().md) method, then modify that snapshot to reflect the new state of the data that you want to display.

For example, the following code creates an empty snapshot and populates it with a single section with three items. Then, the code applies the snapshot, animating the UI updates between the previous state and the new state.

```swift
// Create a snapshot.
var snapshot = NSDiffableDataSourceSnapshot<Int, UUID>()        

// Populate the snapshot.
snapshot.appendSections([0])
snapshot.appendItems([UUID(), UUID(), UUID()])

// Apply the snapshot.
dataSource.apply(snapshot, animatingDifferences: true)
```

For more information, see the diffable data source types:

- [`UICollectionViewDiffableDataSource`](uicollectionviewdiffabledatasource-9tqpa.md)
- [`UITableViewDiffableDataSource`](uitableviewdiffabledatasource-2euir.md)
- [`NSCollectionViewDiffableDataSource`](https://developer.apple.com/documentation/AppKit/NSCollectionViewDiffableDataSource-axww)

##### Bridging

You can bridge from an [`NSDiffableDataSourceSnapshotReference`](nsdiffabledatasourcesnapshotreference.md) object to this type:

```swift
let snapshot = snapshotReference as NSDiffableDataSourceSnapshot<Int, UUID>
```

## Topics

### Creating a snapshot
- [init()](nsdiffabledatasourcesnapshot-swift.struct/init.md)
  Creates an empty snapshot.
- [func appendSections([SectionIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/appendsections(_:).md)
  Adds the sections with the specified identifiers to the snapshot.
- [func appendItems([ItemIdentifierType], toSection: SectionIdentifierType?)](nsdiffabledatasourcesnapshot-swift.struct/appenditems(_:tosection:).md)
  Adds the items with the specified identifiers to the specified section of the snapshot.
### Getting item and section metrics
- [var numberOfItems: Int](nsdiffabledatasourcesnapshot-swift.struct/numberofitems.md)
  The number of items in the snapshot.
- [var numberOfSections: Int](nsdiffabledatasourcesnapshot-swift.struct/numberofsections.md)
  The number of sections in the snapshot.
- [func numberOfItems(inSection: SectionIdentifierType) -> Int](nsdiffabledatasourcesnapshot-swift.struct/numberofitems(insection:).md)
  Returns the number of items in the specified section of the snapshot.
### Identifying items and sections
- [var itemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [SectionIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func indexOfItem(ItemIdentifierType) -> Int?](nsdiffabledatasourcesnapshot-swift.struct/indexofitem(_:).md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func indexOfSection(SectionIdentifierType) -> Int?](nsdiffabledatasourcesnapshot-swift.struct/indexofsection(_:).md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiers(inSection: SectionIdentifierType) -> [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/itemidentifiers(insection:).md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(containingItem: ItemIdentifierType) -> SectionIdentifierType?](nsdiffabledatasourcesnapshot-swift.struct/sectionidentifier(containingitem:).md)
  Returns the identifier of the section containing the specified item in the snapshot.
### Inserting items and sections
- [func insertItems([ItemIdentifierType], afterItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:afteritem:).md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems([ItemIdentifierType], beforeItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:beforeitem:).md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], afterSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:aftersection:).md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], beforeSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:beforesection:).md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.
### Removing items and sections
- [func deleteAllItems()](nsdiffabledatasourcesnapshot-swift.struct/deleteallitems.md)
  Deletes all of the items from the snapshot.
- [func deleteItems([ItemIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/deleteitems(_:).md)
  Deletes the items with the specified identifiers from the snapshot.
- [func deleteSections([SectionIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/deletesections(_:).md)
  Deletes the sections with the specified identifiers from the snapshot.
### Reordering items and sections
- [func moveItem(ItemIdentifierType, afterItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:afteritem:).md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(ItemIdentifierType, beforeItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:beforeitem:).md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(SectionIdentifierType, afterSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/movesection(_:aftersection:).md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(SectionIdentifierType, beforeSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/movesection(_:beforesection:).md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.
### Reloading data
- [func reconfigureItems([ItemIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reconfigureitems(_:).md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems([ItemIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reloaditems(_:).md)
  Reloads the data within the specified items in the snapshot.
- [var reloadedItemIdentifiers: [ItemIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [func reloadSections([SectionIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/reloadsections(_:).md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [SectionIdentifierType]](nsdiffabledatasourcesnapshot-swift.struct/reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.
### Supporting bridging
- [class NSDiffableDataSourceSnapshotReference](nsdiffabledatasourcesnapshotreference.md)
  A representation of the state of the data in a view at a specific point in time.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Updating collection views using diffable data sources](updating-collection-views-using-diffable-data-sources.md)
  Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
- [class UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md)
  The object you use to manage data and provide cells for a collection view.
- [protocol UICollectionViewDataSource](uicollectionviewdatasource.md)
  The methods adopted by the object you use to manage data and provide cells for a collection view.
- [protocol UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
- [struct NSDiffableDataSourceSectionSnapshot](nsdiffabledatasourcesectionsnapshot-swift.struct.md)
  A representation of the state of the data in a layout section at a specific point in time.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct)*