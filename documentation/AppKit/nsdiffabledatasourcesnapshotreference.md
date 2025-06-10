# NSDiffableDataSourceSnapshotReference

**Framework**: AppKit  
**Kind**: class

A representation of the state of the data in a view at a specific point in time.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NSDiffableDataSourceSnapshotReference
```

#### Overview

> ❗ **Important**:  If you’re working in a Swift codebase, always use [`NSDiffableDataSourceSnapshot`](nsdiffabledatasourcesnapshot-swift.struct.md) instead of `NSDiffableDataSourceSnapshotReference`.

Diffable data sources use  to provide data for collection views and table views. Through a snapshot, you set up the initial state of the data that displays in a view, and later update that data.

The data in a snapshot is made up of the sections and items you want to display, in the specific order you want to display them. You configure what to display by adding, deleting, or moving the sections and items.

> ❗ **Important**:  Each of your sections and items must have unique identifiers.

To display data in a view using a snapshot:

1. Create a snapshot and populate it with the state of the data you want to display.
2. Apply the snapshot to reflect the changes in the UI.

You can create and configure a snapshot in one of these ways:

- Create an empty snapshot, then append sections and items to it.
- Get the current snapshot by calling the diffable data source’s [`snapshot()`](nscollectionviewdiffabledatasourcereference/snapshot().md) method, then modify that snapshot to reflect the new state of the data that you want to display.

For example, the following code creates an empty snapshot, and populates it with a single section with three items. Then, it applies the snapshot, animating the UI updates between the previous state and the new state represented in the snapshot.

For more information, see the diffable data source types:

- [`UICollectionViewDiffableDataSource`](https://developer.apple.com/documentation/UIKit/UICollectionViewDiffableDataSource-9tqpa)
- [`UITableViewDiffableDataSource`](https://developer.apple.com/documentation/UIKit/UITableViewDiffableDataSource-2euir)
- [`NSCollectionViewDiffableDataSourceReference`](nscollectionviewdiffabledatasourcereference.md)

##### Bridging

Avoid using this type in Swift code. Only use this type to bridge from Objective-C code to Swift code by typecasting from a snapshot reference to a snapshot:

```swift
let snapshot = snapshotReference as NSDiffableDataSourceSnapshot<Int, UUID>
```

## Topics

### Creating a snapshot
- [func appendSections(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/appendsections(withidentifiers:).md)
  Adds the sections with the specified identifiers to the snapshot.
- [func appendItems(withIdentifiers: [Any], intoSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/appenditems(withidentifiers:intosectionwithidentifier:).md)
  Adds the items with the specified identifiers to the specified section of the snapshot.
- [func appendItems(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/appenditems(withidentifiers:).md)
  Adds the items with the specified identifiers to the last section of the snapshot.
### Getting item and section metrics
- [var numberOfItems: Int](nsdiffabledatasourcesnapshotreference/numberofitems.md)
  The number of items in the snapshot.
- [var numberOfSections: Int](nsdiffabledatasourcesnapshotreference/numberofsections.md)
  The number of sections in the snapshot.
- [func numberOfItems(inSection: Any) -> Int](nsdiffabledatasourcesnapshotreference/numberofitems(insection:).md)
  Returns the number of items in the specified section of the snapshot.
### Identifying items and sections
- [var itemIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/itemidentifiers.md)
  The identifiers of all of the items in the snapshot.
- [var sectionIdentifiers: [Any]](nsdiffabledatasourcesnapshotreference/sectionidentifiers.md)
  The identifiers of all of the sections in the snapshot.
- [func index(ofItemIdentifier: Any) -> Int](nsdiffabledatasourcesnapshotreference/index(ofitemidentifier:).md)
  Returns the index of the item in the snapshot with the specified identifier.
- [func index(ofSectionIdentifier: Any) -> Int](nsdiffabledatasourcesnapshotreference/index(ofsectionidentifier:).md)
  Returns the index of the section of the snapshot with the specified identifier.
- [func itemIdentifiersInSection(withIdentifier: Any) -> [Any]](nsdiffabledatasourcesnapshotreference/itemidentifiersinsection(withidentifier:).md)
  Returns the identifiers of all of the items in the specified section of the snapshot.
- [func sectionIdentifier(forSectionContainingItemIdentifier: Any) -> Any?](nsdiffabledatasourcesnapshotreference/sectionidentifier(forsectioncontainingitemidentifier:).md)
  Returns the identifier of the section containing the specified item in the snapshot.
### Inserting items and sections
- [func insertItems(withIdentifiers: [Any], afterItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:afteritemwithidentifier:).md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems(withIdentifiers: [Any], beforeItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertitems(withidentifiers:beforeitemwithidentifier:).md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], afterSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:aftersectionwithidentifier:).md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections(withIdentifiers: [Any], beforeSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/insertsections(withidentifiers:beforesectionwithidentifier:).md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.
### Removing items and sections
- [func deleteAllItems()](nsdiffabledatasourcesnapshotreference/deleteallitems.md)
  Deletes all of the items from the snapshot.
- [func deleteItems(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/deleteitems(withidentifiers:).md)
  Deletes the items with the specified identifiers from the snapshot.
- [func deleteSections(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/deletesections(withidentifiers:).md)
  Deletes the sections with the specified identifiers from the snapshot.
### Reordering items and sections
- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:).md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(withIdentifier: Any, beforeItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:beforeitemwithidentifier:).md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(withIdentifier: Any, afterSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/movesection(withidentifier:aftersectionwithidentifier:).md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(withIdentifier: Any, beforeSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/movesection(withidentifier:beforesectionwithidentifier:).md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.
### Reloading data
- [func reloadItems(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/reloaditems(withidentifiers:).md)
  Reloads the data within the specified items in the snapshot.
- [func reloadSections(withIdentifiers: [Any])](nsdiffabledatasourcesnapshotreference/reloadsections(withidentifiers:).md)
  Reloads the data within the specified sections of the snapshot.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference)*