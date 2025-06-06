# insertItems(_:afterItem:)

**Framework**: UIKit  
**Kind**: method

Inserts the provided items immediately after the item with the specified identifier in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
mutating func insertItems(_ identifiers: [ItemIdentifierType], afterItem afterIdentifier: ItemIdentifierType)
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to add to the snapshot.
- `afterIdentifier`: The identifier of the item after which to insert the new items.

## See Also

- [func insertItems([ItemIdentifierType], beforeItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:beforeitem:).md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], afterSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:aftersection:).md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], beforeSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:beforesection:).md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:afteritem:))*