# NSDiffableDataSourceSectionSnapshotReference

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A representation of the state of the data in a layout section at a specific point in time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class NSDiffableDataSourceSectionSnapshotReference
```

```objc
@interface NSDiffableDataSourceSectionSnapshot : NSObject
```

## Overview

A section snapshot represents the data for a single section in a collection view. Through a section snapshot, you set up the initial state of the data that displays in an individual section of your view, and later update that data.

You can use section snapshots with or instead of an [`NSDiffableDataSourceSnapshotReference`](./nsdiffabledatasourcesnapshotreference.md), which represents the data in the entire view. Use a section snapshot when you need precise management of the data in a section of your layout, such as when the sections of your layout acquire their data from different sources. You can also use a section snapshot to represent data with a hierarchical structure, such as an outline with expandable items.

The following example creates a section snapshot with one root item that contains three child items:

```objc
for (NSNumber *section in sections) {
    // Create a section snapshot.
    NSDiffableDataSourceSectionSnapshot<NSString *> *sectionSnapshot = [[NSDiffableDataSourceSectionSnapshot alloc] init];
    
    // Populate the section snapshot.
    [sectionSnapshot appendItems: @[@"Food", @"Drinks"]];
    [sectionSnapshot appendItems: @[@"🍏", @"🍓", @"🥐"] intoParentItem: @"Food"];
    
    // Apply the section snapshot.
    [dataSource applySnapshot: sectionSnapshot
                    toSection: section
         animatingDifferences: YES];
}
```

> ❗ **Important**: If you’re working in a Swift codebase, always use [`NSDiffableDataSourceSectionSnapshot`](./nsdiffabledatasourcesectionsnapshot-swift.struct.md) instead.

Avoid using this type in Swift code. Only use this type to bridge from Objective-C code to Swift code by typecasting from a section snapshot reference to a section snapshot:

```swift
let sectionSnapshot = sectionSnapshotRef as NSDiffableDataSourceSectionSnapshot<UUID>
```

## Topics

### Creating a section snapshot
- [init()](./nsdiffabledatasourcesectionsnapshotreference/init%28%29.md)
  Creates an empty section snapshot.
- [func ofParentItem(Any) -> NSDiffableDataSourceSectionSnapshotReference](./nsdiffabledatasourcesectionsnapshotreference/ofparentitem%28_%29.md)
  Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.
- [func ofParentItem(Any, includingParentItem: Bool) -> NSDiffableDataSourceSectionSnapshotReference](./nsdiffabledatasourcesectionsnapshotreference/ofparentitem%28_,includingparentitem%29.md)
  Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [func appendItems([Any])](./nsdiffabledatasourcesectionsnapshotreference/appenditems%28_%29.md)
  Adds the specified items to the section snapshot.
- [func appendItems([Any], intoParentItem: Any?)](./nsdiffabledatasourcesectionsnapshotreference/appenditems%28_,intoparentitem%29.md)
  Adds the specified items as child items of the specified parent item in the section snapshot.
### Accessing items
- [var items: [Any]](./nsdiffabledatasourcesectionsnapshotreference/items.md)
  The identifiers of all items in the section snapshot.
- [var rootItems: [Any]](./nsdiffabledatasourcesectionsnapshotreference/rootitems.md)
  The identifiers of the items at the top level of the section snapshot’s hierarchy.
- [var visibleItems: [Any]](./nsdiffabledatasourcesectionsnapshotreference/visibleitems.md)
  The identifiers of the currently visible items in the section snapshot.
### Getting item metrics
- [func index(ofItem: Any) -> Int](./nsdiffabledatasourcesectionsnapshotreference/index%28ofitem%29.md)
  Finds the index of the specified item in the section snapshot.
- [func level(ofItem: Any) -> Int](./nsdiffabledatasourcesectionsnapshotreference/level%28ofitem%29.md)
  Finds the hierarchical level of the specified item in the section snapshot.
- [func parent(ofChildItem: Any) -> Any?](./nsdiffabledatasourcesectionsnapshotreference/parent%28ofchilditem%29.md)
  Finds the parent item of the specified item in the section snapshot.
- [func containsItem(Any) -> Bool](./nsdiffabledatasourcesectionsnapshotreference/containsitem%28_%29.md)
  Indicates whether the section snapshot contains the specified item.
- [func isVisible(Any) -> Bool](./nsdiffabledatasourcesectionsnapshotreference/isvisible%28_%29.md)
  Indicates whether the specified item is currently visible onscreen.
### Inserting items
- [func insert(NSDiffableDataSourceSectionSnapshotReference, afterItem: Any) -> Any](./nsdiffabledatasourcesectionsnapshotreference/insert%28_,afteritem%29.md)
  Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [func insertItems([Any], afterItem: Any)](./nsdiffabledatasourcesectionsnapshotreference/insertitems%28_,afteritem%29.md)
  Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [func insert(NSDiffableDataSourceSectionSnapshotReference, beforeItem: Any)](./nsdiffabledatasourcesectionsnapshotreference/insert%28_,beforeitem%29.md)
  Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.
- [func insertItems([Any], beforeItem: Any)](./nsdiffabledatasourcesectionsnapshotreference/insertitems%28_,beforeitem%29.md)
  Inserts the provided items immediately before the item with the specified identifier in the section snapshot.
### Removing items
- [func deleteItems([Any])](./nsdiffabledatasourcesectionsnapshotreference/deleteitems%28_%29.md)
  Deletes the items with the specified identifiers, and any of their child items, from the section snapshot.
- [func deleteAllItems()](./nsdiffabledatasourcesectionsnapshotreference/deleteallitems%28%29.md)
  Deletes all of the items from the section snapshot.
### Replacing items
- [func replaceChildren(ofParentItem: Any, with: NSDiffableDataSourceSectionSnapshotReference)](./nsdiffabledatasourcesectionsnapshotreference/replacechildren%28ofparentitem,with%29.md)
  Replaces all child items of the specified parent item with the provided section snapshot.
### Expanding and collapsing items
- [func isExpanded(Any) -> Bool](./nsdiffabledatasourcesectionsnapshotreference/isexpanded%28_%29.md)
  Indicates whether the item with the specified identifier is in an expanded state.
- [func expandItems([Any])](./nsdiffabledatasourcesectionsnapshotreference/expanditems%28_%29.md)
  Expands the specified items in the section snapshot.
- [func collapseItems([Any])](./nsdiffabledatasourcesectionsnapshotreference/collapseitems%28_%29.md)
  Collapses the specified items in the section snapshot.
### Debugging section snapshots
- [func visualDescription() -> String](./nsdiffabledatasourcesectionsnapshotreference/visualdescription%28%29.md)
  Returns a string with an ASCII representation of the section snapshot.
### Instance Methods
- [func expandedItems() -> [Any]](./nsdiffabledatasourcesectionsnapshotreference/expandeditems%28%29.md)
  The identifiers of all expanded items in the section snapshot.

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
- [NSDiffableDataSourceSnapshot](./nsdiffabledatasourcesnapshotreference.md)
  A representation of the state of the data in a view at a specific point in time.
- [UIRefreshControl](./uirefreshcontrol.md)
  A standard control that can initiate the refreshing of a scroll view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference)*