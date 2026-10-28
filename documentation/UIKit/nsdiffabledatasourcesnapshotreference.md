# NSDiffableDataSourceSnapshotReference

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A representation of the state of the data in a view at a specific point in time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class NSDiffableDataSourceSnapshotReference
```

```objc
@interface NSDiffableDataSourceSnapshot : NSObject
```

## Overview

Diffable data sources use *snapshots* to provide data for collection views and table views. You use a snapshot to set up the initial state of the data that a view displays, and you use snapshots to reflect changes to the data that the view displays.

The data in a snapshot is made up of the sections and items you want to display, in the order that you determine. You configure what to display by adding, deleting, or moving the sections and items.

> ❗ **Important**:  Each of your sections and items must have unique identifiers that conform to the [`Hashable`](../Swift/hashable.md) protocol. Use `struct` or `enum` Swift value types for your identifiers, including built-in types such as `Int`, `String`, or `UUID`. If you use a Swift `class` for your identifiers, your `class` must be a subclass of `NSObject`.

To display data in a view using a snapshot:

1. Create a snapshot and populate it with the state of the data you want to display.
2. Apply the snapshot to reflect the changes in the UI.

You can create and configure a snapshot in one of these ways:

- Create an empty snapshot, then append sections and items to it.
- Get the current snapshot by calling the diffable data source’s [`snapshot()`](./uicollectionviewdiffabledatasource-9tqpa/snapshot%28%29.md) method, then modify that snapshot to reflect the new state of the data that you want to display.

For example, the following code creates an empty snapshot and populates it with a single section with three items. Then, the code applies the snapshot, animating the UI updates between the previous state and the new state.

```objc
// Create a snapshot.
NSDiffableDataSourceSnapshot<NSNumber *, NSUUID *> *snapshot = [[NSDiffableDataSourceSnapshot alloc] init];


// Populate the snapshot.
[snapshot appendSectionsWithIdentifiers:@[@0]];
[snapshot appendItemsWithIdentifiers:@[[NSUUID UUID], [NSUUID UUID], [NSUUID UUID]]];


// Apply the snapshot.
[self.dataSource applySnapshot:snapshot animatingDifferences:YES];
```

For more information, see the diffable data source types:

- [`UICollectionViewDiffableDataSourceReference`](./uicollectionviewdiffabledatasourcereference.md)
- [`UITableViewDiffableDataSourceReference`](./uitableviewdiffabledatasourcereference.md)
- [`NSCollectionViewDiffableDataSource`](../AppKit/nscollectionviewdiffabledatasource-axww.md)

> ❗ **Important**: If you’re working in a Swift codebase, always use [`NSDiffableDataSourceSnapshot`](./nsdiffabledatasourcesnapshot-swift.struct.md) instead.

Avoid using this type in Swift code. Only use this type to bridge from Objective-C code to Swift code by typecasting from a snapshot reference to a snapshot:

```swift
let snapshot = snapshotReference as NSDiffableDataSourceSnapshot<Int, UUID>
```

## Topics

### Creating a snapshot
- [func appendSections(withIdentifiers: [Any])](./nsdiffabledatasourcesnapshotreference/appendsections%28withidentifiers%29.md)
  Adds the sections with the specified identifiers to the snapshot.
- [func appendItems(withIdentifiers: [Any], intoSectionWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/appenditems%28withidentifiers,intosectionwithidentifier%29.md)
  Adds the items with the specified identifiers to the specified section of the snapshot.
- [func appendItems(withIdentifiers: [Any])](./nsdiffabledatasourcesnapshotreference/appenditems%28withidentifiers%29.md)
  Adds the items with the specified identifiers to the last section of the snapshot.
### Getting item and section metrics
- [var numberOfItems: Int](./nsdiffabledatasourcesnapshotreference/numberofitems.md)
  The number of items in the snapshot.
- [var numberOfSections: Int](./nsdiffabledatasourcesnapshotreference/numberofsections.md)
  The number of sections in the snapshot.
- [func numberOfItems(inSection: Any) -> Int](./nsdiffabledatasourcesnapshotreference/numberofitems%28insection%29.md)
  Returns the number of items in the specified section of the snapshot.
### Identifying items and sections
- [var itemIdentifiers: [Any]](./nsdiffabledatasourcesnapshotreference/itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [Any]](./nsdiffabledatasourcesnapshotreference/sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func index(ofItemIdentifier: Any) -> Int](./nsdiffabledatasourcesnapshotreference/index%28ofitemidentifier%29.md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func index(ofSectionIdentifier: Any) -> Int](./nsdiffabledatasourcesnapshotreference/index%28ofsectionidentifier%29.md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiersInSection(withIdentifier: Any) -> [Any]](./nsdiffabledatasourcesnapshotreference/itemidentifiersinsection%28withidentifier%29.md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(forSectionContainingItemIdentifier: Any) -> Any?](./nsdiffabledatasourcesnapshotreference/sectionidentifier%28forsectioncontainingitemidentifier%29.md)
  Returns the identifier of the section containing the specified item in the snapshot.
### Inserting items and sections
- [func insertItems(withIdentifiers: [Any], afterItemWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/insertitems%28withidentifiers,afteritemwithidentifier%29.md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems(withIdentifiers: [Any], beforeItemWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/insertitems%28withidentifiers,beforeitemwithidentifier%29.md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], afterSectionWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/insertsections%28withidentifiers,aftersectionwithidentifier%29.md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], beforeSectionWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/insertsections%28withidentifiers,beforesectionwithidentifier%29.md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.
### Removing items and sections
- [func deleteAllItems()](./nsdiffabledatasourcesnapshotreference/deleteallitems%28%29.md)
  Deletes all of the items from the snapshot.
- [func deleteItems(withIdentifiers: [Any])](./nsdiffabledatasourcesnapshotreference/deleteitems%28withidentifiers%29.md)
  Deletes the items with the specified identifiers from the snapshot.
- [func deleteSections(withIdentifiers: [Any])](./nsdiffabledatasourcesnapshotreference/deletesections%28withidentifiers%29.md)
  Deletes the sections with the specified identifiers from the snapshot.
### Reordering items and sections
- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/moveitem%28withidentifier,afteritemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(withIdentifier: Any, beforeItemWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/moveitem%28withidentifier,beforeitemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(withIdentifier: Any, afterSectionWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/movesection%28withidentifier,aftersectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(withIdentifier: Any, beforeSectionWithIdentifier: Any)](./nsdiffabledatasourcesnapshotreference/movesection%28withidentifier,beforesectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.
### Reloading data
- [func reconfigureItems(withIdentifiers: [Any])](./nsdiffabledatasourcesnapshotreference/reconfigureitems%28withidentifiers%29.md)
  Updates the data for the items you specify in the snapshot, preserving the existing cells for the items.
- [var reconfiguredItemIdentifiers: [Any]](./nsdiffabledatasourcesnapshotreference/reconfigureditemidentifiers.md)
  Identifies the items reconfigured by the changes to the snapshot.
- [func reloadItems(withIdentifiers: [Any])](./nsdiffabledatasourcesnapshotreference/reloaditems%28withidentifiers%29.md)
  Reloads the data within the specified items in the snapshot.
- [var reloadedItemIdentifiers: [Any]](./nsdiffabledatasourcesnapshotreference/reloadeditemidentifiers.md)
  Identifies the items reloaded by the changes to the snapshot.
- [func reloadSections(withIdentifiers: [Any])](./nsdiffabledatasourcesnapshotreference/reloadsections%28withidentifiers%29.md)
  Reloads the data within the specified sections of the snapshot.
- [var reloadedSectionIdentifiers: [Any]](./nsdiffabledatasourcesnapshotreference/reloadedsectionidentifiers.md)
  Identifies the sections reloaded by the changes to the snapshot.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Data
- [Updating collection views using diffable data sources](./updating-collection-views-using-diffable-data-sources.md)
  Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](./implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [Building high-performance lists and collection views](./building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.
- [UICollectionViewDiffableDataSource](./uicollectionviewdiffabledatasourcereference.md)
  The object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSource](./uicollectionviewdatasource.md)
  The methods adopted by the object you use to manage data and provide cells for a collection view.
- [UICollectionViewDataSourcePrefetching](./uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.
- [NSDiffableDataSourceSectionSnapshot](./nsdiffabledatasourcesectionsnapshotreference.md)
  A representation of the state of the data in a layout section at a specific point in time.
- [UIRefreshControl](./uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference)*