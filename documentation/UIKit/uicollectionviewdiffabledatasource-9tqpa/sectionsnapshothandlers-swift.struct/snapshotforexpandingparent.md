# snapshotForExpandingParent

**Framework**: UIKit  
**Kind**: property

The handler that provides the section snapshot for expanding the parent item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var snapshotForExpandingParent: ((ItemIdentifierType, NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)? { get set }
```

#### Discussion

Use the [`snapshotForExpandingParent`](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.md) handler to customize the snapshot that returns when a particular parent item is expanded.

```swift
// Allow every item to be collapsed
dataSource.sectionSnapshotHandlers.shouldCollapseItem = { item in return true }

dataSource.sectionSnapshotHandlers.snapshotForExpandingParent = {
    parent, existingSnapshot -> NSDiffableDataSourceSectionSnapshot<String> in
    
    // Return child snapshot for the parent, or just existingSnapshot
}
```

## See Also

- [var shouldCollapseItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldcollapseitem.md)
  The handler that determines whether a particular item is collapsable.
- [var shouldExpandItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldexpanditem.md)
  The handler that determines whether a particular item is expandable.
- [var willCollapseItem: ((ItemIdentifierType) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willcollapseitem.md)
  The handler that prepares the diffable data source for collapsing an item.
- [var willExpandItem: ((ItemIdentifierType) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willexpanditem.md)
  The handler that prepares the diffable data source for expanding an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent)*