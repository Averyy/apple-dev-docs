# sectionSnapshotHandlers

**Framework**: UIKit  
**Kind**: property

The diffable data source’s handlers for expanding and collapsing items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var sectionSnapshotHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionSnapshotHandlers<ItemIdentifierType> { get set }
```

#### Discussion

Provide section snapshot handlers to support the expanding or collapsing of items in your collection view.

Use the [`snapshotForExpandingParent`](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.md) handler to customize the snapshot that returns when a particular parent item is expanded.

```swift
// Allow every item to be collapsed
dataSource.sectionSnapshotHandlers.shouldCollapseItem = { item in return true }

dataSource.sectionSnapshotHandlers.snapshotForExpandingParent = {
    parent, currentChildSnapshot -> NSDiffableDataSourceSectionSnapshot<String> in
    
    // Return child snapshot for the parent, or just currentChildSnapshot
}
```

## See Also

- [UICollectionViewDiffableDataSource.SectionSnapshotHandlers](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct.md)
  Handlers for expanding and collapsing items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.property)*