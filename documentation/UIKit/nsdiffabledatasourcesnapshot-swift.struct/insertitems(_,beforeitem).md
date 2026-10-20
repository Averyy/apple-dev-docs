# insertItems(_:beforeItem:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided items immediately before the item with the specified identifier in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
mutating func insertItems(_ identifiers: [ItemIdentifierType], beforeItem beforeIdentifier: ItemIdentifierType)
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to add to the snapshot.
- `beforeIdentifier`: The identifier of the item before which to insert the new items.

## See Also

### Inserting items and sections
- [func insertItems([ItemIdentifierType], afterItem: ItemIdentifierType)](./insertitems%28_,afteritem%29.md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], afterSection: SectionIdentifierType)](./insertsections%28_,aftersection%29.md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], beforeSection: SectionIdentifierType)](./insertsections%28_,beforesection%29.md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:beforeitem:))*