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
@MainActor var reorderingHandlers: __UICollectionViewDiffableDataSourceReorderingHandlers { get set }
```

#### Discussion

Provide reordering handlers to support the reordering of items in your collection view.

The system calls the [`didReorderHandler`](uicollectionviewdiffabledatasourcereorderinghandlers/didreorderhandler.md) handler after a reordering transaction ([`NSDiffableDataSourceTransaction`](nsdiffabledatasourcetransaction-swift.struct.md)) occurs, so you can update your data backing store with information about the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/reorderinghandlers)*