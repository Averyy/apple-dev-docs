# NSDiffableDataSourceSectionSnapshotReference

**Framework**: UIKit  
**Kind**: class

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

#### Overview

A section snapshot represents the data for a single section in a collection view. Through a section snapshot, you set up the initial state of the data that displays in an individual section of your view, and later update that data.

You can use section snapshots with or instead of an [`NSDiffableDataSourceSnapshotReference`](nsdiffabledatasourcesnapshotreference.md), which represents the data in the entire view. Use a section snapshot when you need precise management of the data in a section of your layout, such as when the sections of your layout acquire their data from different sources. You can also use a section snapshot to represent data with a hierarchical structure, such as an outline with expandable items.

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

> ❗ **Important**: If you’re working in a Swift codebase, always use [`NSDiffableDataSourceSectionSnapshot`](nsdiffabledatasourcesectionsnapshot-swift.struct.md) instead.

Avoid using this type in Swift code. Only use this type to bridge from Objective-C code to Swift code by typecasting from a section snapshot reference to a section snapshot:

```swift
let sectionSnapshot = sectionSnapshotRef as NSDiffableDataSourceSectionSnapshot<UUID>
```

## Topics

### Creating a section snapshot
- [init()](nsdiffabledatasourcesectionsnapshotreference/init.md)
  Creates an empty section snapshot.
- [func ofParentItem(Any) -> NSDiffableDataSourceSectionSnapshotReference](nsdiffabledatasourcesectionsnapshotreference/ofparentitem(_:).md)
  Creates a section snapshot containing the child items of the specified parent item, excluding the parent item.
- [func ofParentItem(Any, includingParentItem: Bool) -> NSDiffableDataSourceSectionSnapshotReference](nsdiffabledatasourcesectionsnapshotreference/ofparentitem(_:includingparentitem:).md)
  Creates a section snapshot containing the child items of the specified parent item, including the parent item.
- [func appendItems([Any])](nsdiffabledatasourcesectionsnapshotreference/appenditems(_:).md)
  Adds the specified items to the section snapshot.
- [func appendItems([Any], intoParentItem: Any?)](nsdiffabledatasourcesectionsnapshotreference/appenditems(_:intoparentitem:).md)
  Adds the specified items as child items of the specified parent item in the section snapshot.
### Accessing items
- [var items: [Any]](nsdiffabledatasourcesectionsnapshotreference/items.md)
  The identifiers of all items in the section snapshot.
- [var rootItems: [Any]](nsdiffabledatasourcesectionsnapshotreference/rootitems.md)
  The identifiers of the items at the top level of the section snapshot’s hierarchy.
- [var visibleItems: [Any]](nsdiffabledatasourcesectionsnapshotreference/visibleitems.md)
  The identifiers of the currently visible items in the section snapshot.
### Getting item metrics
- [func index(ofItem: Any) -> Int](nsdiffabledatasourcesectionsnapshotreference/index(ofitem:).md)
  Finds the index of the specified item in the section snapshot.
- [func level(ofItem: Any) -> Int](nsdiffabledatasourcesectionsnapshotreference/level(ofitem:).md)
  Finds the hierarchical level of the specified item in the section snapshot.
- [func parent(ofChildItem: Any) -> Any?](nsdiffabledatasourcesectionsnapshotreference/parent(ofchilditem:).md)
  Finds the parent item of the specified item in the section snapshot.
- [func containsItem(Any) -> Bool](nsdiffabledatasourcesectionsnapshotreference/containsitem(_:).md)
  Indicates whether the section snapshot contains the specified item.
- [func isVisible(Any) -> Bool](nsdiffabledatasourcesectionsnapshotreference/isvisible(_:).md)
  Indicates whether the specified item is currently visible onscreen.
### Inserting items
- [func insert(NSDiffableDataSourceSectionSnapshotReference, afterItem: Any) -> Any](nsdiffabledatasourcesectionsnapshotreference/insert(_:afteritem:).md)
  Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [func insertItems([Any], afterItem: Any)](nsdiffabledatasourcesectionsnapshotreference/insertitems(_:afteritem:).md)
  Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [func insert(NSDiffableDataSourceSectionSnapshotReference, beforeItem: Any)](nsdiffabledatasourcesectionsnapshotreference/insert(_:beforeitem:).md)
  Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.
- [func insertItems([Any], beforeItem: Any)](nsdiffabledatasourcesectionsnapshotreference/insertitems(_:beforeitem:).md)
  Inserts the provided items immediately before the item with the specified identifier in the section snapshot.
### Removing items
- [func deleteItems([Any])](nsdiffabledatasourcesectionsnapshotreference/deleteitems(_:).md)
  Deletes the items with the specified identifiers, and any of their child items, from the section snapshot.
- [func deleteAllItems()](nsdiffabledatasourcesectionsnapshotreference/deleteallitems.md)
  Deletes all of the items from the section snapshot.
### Replacing items
- [func replaceChildren(ofParentItem: Any, with: NSDiffableDataSourceSectionSnapshotReference)](nsdiffabledatasourcesectionsnapshotreference/replacechildren(ofparentitem:with:).md)
  Replaces all child items of the specified parent item with the provided section snapshot.
### Expanding and collapsing items
- [func isExpanded(Any) -> Bool](nsdiffabledatasourcesectionsnapshotreference/isexpanded(_:).md)
  Indicates whether the item with the specified identifier is in an expanded state.
- [func expandItems([Any])](nsdiffabledatasourcesectionsnapshotreference/expanditems(_:).md)
  Expands the specified items in the section snapshot.
- [func collapseItems([Any])](nsdiffabledatasourcesectionsnapshotreference/collapseitems(_:).md)
  Collapses the specified items in the section snapshot.
### Debugging section snapshots
- [func visualDescription() -> String](nsdiffabledatasourcesectionsnapshotreference/visualdescription.md)
  Returns a string with an ASCII representation of the section snapshot.
### Instance Methods
- [func expandedItems() -> [Any]](nsdiffabledatasourcesectionsnapshotreference/expandeditems.md)
  The identifiers of all expanded items in the section snapshot.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference)*