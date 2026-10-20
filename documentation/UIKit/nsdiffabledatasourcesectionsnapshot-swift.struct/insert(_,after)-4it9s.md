# insert(_:after:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
mutating func insert(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, after item: ItemIdentifierType)
```

## See Also

### Inserting items
- [func insert([ItemIdentifierType], after: ItemIdentifierType)](./insert%28_,after%29-9v9c7.md)
  Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [func insert([ItemIdentifierType], before: ItemIdentifierType)](./insert%28_,before%29-5o91y.md)
  Inserts the provided items immediately before the item with the specified identifier in the section snapshot.
- [func insert(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, before: ItemIdentifierType)](./insert%28_,before%29-bsrn.md)
  Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/insert(_:after:)-4it9s)*