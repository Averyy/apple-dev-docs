# NSDiffableDataSourceSectionSnapshot

**Framework**: UIKit  
**Kind**: struct

A representation of the state of the data in a layout section at a specific point in time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
struct NSDiffableDataSourceSectionSnapshot<ItemIdentifierType> where ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

#### Overview

A section snapshot represents the data for a single section in a collection view. Through a section snapshot, you set up the initial state of the data that displays in an individual section of your view, and later update that data.

You can use section snapshots with or instead of an [`NSDiffableDataSourceSnapshot`](nsdiffabledatasourcesnapshot-swift.struct.md), which represents the data in the entire view. Use a section snapshot when you need precise management of the data in a section of your layout, such as when the sections of your layout acquire their data from different sources. You can also use a section snapshot to represent data with a hierarchical structure, such as an outline with expandable items.

The following example creates a section snapshot with one root item that contains three child items:

```swift
for section in Section.allCases {
    // Create a section snapshot
    var sectionSnapshot = NSDiffableDataSourceSectionSnapshot<String>()
    
    // Populate the section snapshot
    sectionSnapshot.append(["Food", "Drinks"])
    sectionSnapshot.append(["🍏", "🍓", "🥐"], to: "Food")
    
    // Apply the section snapshot
    dataSource.apply(sectionSnapshot,
                     to: section,
                     animatingDifferences: true)
}
```

## Topics

### Creating a section snapshot
- [init()](nsdiffabledatasourcesectionsnapshot-swift.struct/init.md)
  Creates an empty section snapshot.
- [init(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)](nsdiffabledatasourcesectionsnapshot-swift.struct/init(_:).md)
  Creates a copy of the provided section snapshot.
- [func snapshot(of: ItemIdentifierType, includingParent: Bool) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectionsnapshot-swift.struct/snapshot(of:includingparent:).md)
  Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.
- [func append([ItemIdentifierType], to: ItemIdentifierType?)](nsdiffabledatasourcesectionsnapshot-swift.struct/append(_:to:).md)
  Adds the specified items as child items of the specified parent item in the section snapshot.
### Accessing items
- [var items: [ItemIdentifierType]](nsdiffabledatasourcesectionsnapshot-swift.struct/items.md)
  The identifiers of all items in the section snapshot.
- [var rootItems: [ItemIdentifierType]](nsdiffabledatasourcesectionsnapshot-swift.struct/rootitems.md)
  The identifiers of the items at the top level of the section snapshot’s hierarchy.
- [var visibleItems: [ItemIdentifierType]](nsdiffabledatasourcesectionsnapshot-swift.struct/visibleitems.md)
  The identifiers of the currently visible items in the section snapshot.
### Getting item metrics
- [func index(of: ItemIdentifierType) -> Int?](nsdiffabledatasourcesectionsnapshot-swift.struct/index(of:).md)
  Finds the index of the specified item in the section snapshot.
- [func level(of: ItemIdentifierType) -> Int](nsdiffabledatasourcesectionsnapshot-swift.struct/level(of:).md)
  Finds the hierarchical level of the specified item in the section snapshot.
- [func parent(of: ItemIdentifierType) -> ItemIdentifierType?](nsdiffabledatasourcesectionsnapshot-swift.struct/parent(of:).md)
  Finds the parent item of the specified item in the section snapshot.
- [func contains(ItemIdentifierType) -> Bool](nsdiffabledatasourcesectionsnapshot-swift.struct/contains(_:).md)
  Indicates whether the section snapshot contains the specified item.
- [func isVisible(ItemIdentifierType) -> Bool](nsdiffabledatasourcesectionsnapshot-swift.struct/isvisible(_:).md)
  Indicates whether the specified item is currently visible onscreen.
### Inserting items
- [func insert([ItemIdentifierType], after: ItemIdentifierType)](nsdiffabledatasourcesectionsnapshot-swift.struct/insert(_:after:)-9v9c7.md)
  Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [func insert(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, after: ItemIdentifierType)](nsdiffabledatasourcesectionsnapshot-swift.struct/insert(_:after:)-4it9s.md)
  Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [func insert([ItemIdentifierType], before: ItemIdentifierType)](nsdiffabledatasourcesectionsnapshot-swift.struct/insert(_:before:)-5o91y.md)
  Inserts the provided items immediately before the item with the specified identifier in the section snapshot.
- [func insert(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, before: ItemIdentifierType)](nsdiffabledatasourcesectionsnapshot-swift.struct/insert(_:before:)-bsrn.md)
  Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.
### Removing items
- [func delete([ItemIdentifierType])](nsdiffabledatasourcesectionsnapshot-swift.struct/delete(_:).md)
  Deletes the items with the specified identifiers, and any of their child items, from the section snapshot.
- [func deleteAll()](nsdiffabledatasourcesectionsnapshot-swift.struct/deleteall.md)
  Deletes all of the items from the section snapshot.
### Replacing items
- [func replace(childrenOf: ItemIdentifierType, using: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)](nsdiffabledatasourcesectionsnapshot-swift.struct/replace(childrenof:using:).md)
  Replaces all child items of the specified parent item with the provided section snapshot.
### Expanding and collapsing items
- [func isExpanded(ItemIdentifierType) -> Bool](nsdiffabledatasourcesectionsnapshot-swift.struct/isexpanded(_:).md)
  Indicates whether the item with the specified identifier is in an expanded state.
- [func expand([ItemIdentifierType])](nsdiffabledatasourcesectionsnapshot-swift.struct/expand(_:).md)
  Expands the specified items in the section snapshot.
- [func collapse([ItemIdentifierType])](nsdiffabledatasourcesectionsnapshot-swift.struct/collapse(_:).md)
  Collapses the specified items in the section snapshot.
### Debugging section snapshots
- [func visualDescription() -> String](nsdiffabledatasourcesectionsnapshot-swift.struct/visualdescription.md)
  Returns a string with an ASCII representation of the section snapshot.
### Supporting bridging
- [class NSDiffableDataSourceSectionSnapshotReference](nsdiffabledatasourcesectionsnapshotreference.md)
  A representation of the state of the data in a layout section at a specific point in time.
### Instance Properties
- [var expandedItems: [ItemIdentifierType]](nsdiffabledatasourcesectionsnapshot-swift.struct/expandeditems.md)

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
- [struct NSDiffableDataSourceSnapshot](nsdiffabledatasourcesnapshot-swift.struct.md)
  A representation of the state of the data in a view at a specific point in time.
- [class UIRefreshControl](uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct)*