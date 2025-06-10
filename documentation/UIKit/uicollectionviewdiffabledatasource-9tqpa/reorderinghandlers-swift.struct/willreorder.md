# willReorder

**Framework**: UIKit  
**Kind**: property

The handler that prepares the diffable data source for reordering its items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var willReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)? { get set }
```

## See Also

- [var canReorderItem: ((ItemIdentifierType) -> Bool)?](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/canreorderitem.md)
  The handler that determines whether you can reorder a particular item.
- [var didReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/didreorder.md)
  The handler that processes a reordering transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/willreorder)*