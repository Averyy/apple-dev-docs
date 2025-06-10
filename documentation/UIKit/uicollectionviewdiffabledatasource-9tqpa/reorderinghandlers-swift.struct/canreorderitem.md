# canReorderItem

**Framework**: UIKit  
**Kind**: property

The handler that determines whether you can reorder a particular item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var canReorderItem: ((ItemIdentifierType) -> Bool)? { get set }
```

## See Also

- [var willReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/willreorder.md)
  The handler that prepares the diffable data source for reordering its items.
- [var didReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/didreorder.md)
  The handler that processes a reordering transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/canreorderitem)*