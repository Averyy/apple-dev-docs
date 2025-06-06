# reorderingHandlers

**Framework**: UIKit  
**Kind**: property

The diffable data source’s handlers for reordering items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var reorderingHandlers: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ReorderingHandlers { get set }
```

#### Discussion

Provide reordering handlers to support the reordering of items in your collection view.

The system calls the [`didReorder`](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/didreorder.md) handler after a reordering transaction ([`NSDiffableDataSourceTransaction`](nsdiffabledatasourcetransaction-swift.struct.md)) occurs, so you can update your data backing store with information about the changes.

```swift
// Allow every item to be reordered
dataSource.reorderingHandlers.canReorderItem = { item in return true }

// Option 1: Update the backing store from a CollectionDifference
dataSource.reorderingHandlers.didReorder = { [weak self] transaction in
    guard let self = self else { return }
    
    if let updatedBackingStore = self.backingStore.applying(transaction.difference) {
        self.backingStore = updatedBackingStore
    }
}

// Option 2: Update the backing store from the final item identifiers
dataSource.reorderingHandlers.didReorder = { [weak self] transaction in
    guard let self = self else { return }
    
    self.backingStore = transaction.finalSnapshot.itemIdentifiers
}
```

## See Also

- [UICollectionViewDiffableDataSource.ReorderingHandlers](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct.md)
  Handlers for reordering items.
- [struct NSDiffableDataSourceTransaction](nsdiffabledatasourcetransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in the view.
- [struct NSDiffableDataSourceSectionTransaction](nsdiffabledatasourcesectiontransaction-swift.struct.md)
  A transaction that describes the changes after reordering the items in a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.property)*