# UICollectionViewDiffableDataSource.SectionSnapshotHandlers

**Framework**: UIKit  
**Kind**: struct

Handlers for expanding and collapsing items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@preconcurrency
struct SectionSnapshotHandlers<ItemIdentifierType> where ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

## Topics

### Expanding and collapsing items
- [var shouldCollapseItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldcollapseitem.md)
  The handler that determines whether a particular item is collapsable.
- [var shouldExpandItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/shouldexpanditem.md)
  The handler that determines whether a particular item is expandable.
- [var willCollapseItem: ((ItemIdentifierType) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willcollapseitem.md)
  The handler that prepares the diffable data source for collapsing an item.
- [var willExpandItem: ((ItemIdentifierType) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/willexpanditem.md)
  The handler that prepares the diffable data source for expanding an item.
- [var snapshotForExpandingParent: ((ItemIdentifierType, NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)?](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.md)
  The handler that provides the section snapshot for expanding the parent item.
### Initializers
- [init()](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct/init.md)
  Creates a section snapshot handlers structure.

## See Also

- [var sectionSnapshotHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionSnapshotHandlers<ItemIdentifierType>](uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.property.md)
  The diffable data source’s handlers for expanding and collapsing items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct)*