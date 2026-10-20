# canReorderItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The handler that determines whether you can reorder a particular item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var canReorderItem: ((ItemIdentifierType) -> Bool)? { get set }
```

## See Also

### Reordering items
- [var willReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](./willreorder.md)
  The handler that prepares the diffable data source for reordering its items.
- [var didReorder: ((NSDiffableDataSourceTransaction<SectionIdentifierType, ItemIdentifierType>) -> Void)?](./didreorder.md)
  The handler that processes a reordering transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/reorderinghandlers-swift.struct/canreorderitem)*