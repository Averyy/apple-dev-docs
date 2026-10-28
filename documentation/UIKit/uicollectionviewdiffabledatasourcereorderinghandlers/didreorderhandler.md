# didReorderHandler

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The handler that processes a reordering transaction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) void (^didReorderHandler)(NSDiffableDataSourceTransaction<id,id> *);
```

## Discussion

The system calls the [`didReorderHandler`](./didreorderhandler.md) handler after a reordering transaction ([`NSDiffableDataSourceTransaction`](../nsdiffabledatasourcetransaction-swift.struct.md)) occurs, so you can update your data backing store with information about the changes.

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

### Reordering items
- [canReorderItemHandler](./canreorderitemhandler.md)
  The handler that determines whether you can reorder a particular item.
- [willReorderHandler](./willreorderhandler.md)
  The handler that prepares the diffable data source for reordering its items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereorderinghandlers/didreorderhandler)*