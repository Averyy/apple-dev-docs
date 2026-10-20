# UICollectionViewDiffableDataSource.ReorderingHandlers

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Handlers for reordering items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
struct ReorderingHandlers
```

Available when `SectionIdentifierType` conforms to `Hashable`, `SectionIdentifierType` conforms to `Sendable`, `ItemIdentifierType` conforms to `Hashable`, and `ItemIdentifierType` conforms to `Sendable`.

## Topics

### Reordering items
- [var canReorderItem: ((ItemIdentifierType) -> Bool)?](./reorderinghandlers-swift.struct/canreorderitem.md)
  The handler that determines whether you can reorder a particular item.
- [var willReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](./reorderinghandlers-swift.struct/willreorder.md)
  The handler that prepares the diffable data source for reordering its items.
- [var didReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](./reorderinghandlers-swift.struct/didreorder.md)
  The handler that processes a reordering transaction.
### Initializers
- [init()](./reorderinghandlers-swift.struct/init%28%29.md)
  Creates a reordering handlers structure.

## See Also

### Supporting reordering
- [var reorderingHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ReorderingHandlers](./reorderinghandlers-swift.property.md)
  The diffable data source’s handlers for reordering items.
- [struct NSDiffableDataSourceTransaction](../nsdiffabledatasourcetransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in the view.
- [struct NSDiffableDataSourceSectionTransaction](../nsdiffabledatasourcesectiontransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct)*