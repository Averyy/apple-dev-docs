# reorderingHandlers

**Framework**: UIKit  
**Kind**: property

The diffable data source’s handlers for reordering items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var reorderingHandlers: __UICollectionViewDiffableDataSourceReorderingHandlers { get set }
```

#### Discussion

Provide reordering handlers to support the reordering of items in your collection view.

The system calls the [`didReorderHandler`](uicollectionviewdiffabledatasourcereorderinghandlers/didreorderhandler.md) handler after a reordering transaction ([`NSDiffableDataSourceTransaction`](nsdiffabledatasourcetransaction-swift.struct.md)) occurs, so you can update your data backing store with information about the changes.

**Swift**:

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

**Objective-C**:

```objc
// Allow every item to be reordered.
[dataSource.reorderingHandlers setCanReorderItemHandler:^BOOL(NSString *item) {
    return YES;
}];

// Option 1: Update the backing store from a CollectionDifference.
[dataSource.reorderingHandlers setDidReorderHandler:^(NSDiffableDataSourceTransaction<NSNumber *,NSString *> *transaction) {
    NSArray<NSString *> *updatedBackingStore = [backingStore arrayByApplyingDifference: transaction.difference];
    if (updatedBackingStore != nil) {
        backingStore = updatedBackingStore;
    }
}];

// Option 2: Update the backing store from the final item identifiers.
[dataSource.reorderingHandlers setDidReorderHandler:^(NSDiffableDataSourceTransaction<NSNumber *,NSString *> *transaction) {
    backingStore = transaction.finalSnapshot.itemIdentifiers;
}];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/reorderinghandlers)*