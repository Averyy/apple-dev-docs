# UICollectionViewDiffableDataSource.SectionSnapshotHandlers

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Handlers for expanding and collapsing items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
@preconcurrency
struct SectionSnapshotHandlers<ItemIdentifierType> where ItemIdentifierType : Hashable, ItemIdentifierType : Sendable
```

Available when `SectionIdentifierType` conforms to `Hashable`, `SectionIdentifierType` conforms to `Sendable`, `ItemIdentifierType` conforms to `Hashable`, and `ItemIdentifierType` conforms to `Sendable`.

## Topics

### Expanding and collapsing items
- [var shouldCollapseItem: ((ItemIdentifierType) -> Bool)?](./sectionsnapshothandlers-swift.struct/shouldcollapseitem.md)
  The handler that determines whether a particular item is collapsable.
- [var shouldExpandItem: ((ItemIdentifierType) -> Bool)?](./sectionsnapshothandlers-swift.struct/shouldexpanditem.md)
  The handler that determines whether a particular item is expandable.
- [var willCollapseItem: ((ItemIdentifierType) -> Void)?](./sectionsnapshothandlers-swift.struct/willcollapseitem.md)
  The handler that prepares the diffable data source for collapsing an item.
- [var willExpandItem: ((ItemIdentifierType) -> Void)?](./sectionsnapshothandlers-swift.struct/willexpanditem.md)
  The handler that prepares the diffable data source for expanding an item.
- [var snapshotForExpandingParent: ((ItemIdentifierType, NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)?](./sectionsnapshothandlers-swift.struct/snapshotforexpandingparent.md)
  The handler that provides the section snapshot for expanding the parent item.
### Initializers
- [init()](./sectionsnapshothandlers-swift.struct/init%28%29.md)
  Creates a section snapshot handlers structure.

## See Also

### Supporting expanding and collapsing
- [var sectionSnapshotHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SectionSnapshotHandlers<ItemIdentifierType>](./sectionsnapshothandlers-swift.property.md)
  The diffable data source’s handlers for expanding and collapsing items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/sectionsnapshothandlers-swift.struct)*