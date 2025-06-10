# didReorder

**Framework**: UIKit  
**Kind**: property

The handler that processes a reordering transaction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var didReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)? { get set }
```

#### Discussion

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

- [var canReorderItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/canreorderitem.md)
  The handler that determines whether you can reorder a particular item.
- [var willReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/willreorder.md)
  The handler that prepares the diffable data source for reordering its items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/didreorder)*