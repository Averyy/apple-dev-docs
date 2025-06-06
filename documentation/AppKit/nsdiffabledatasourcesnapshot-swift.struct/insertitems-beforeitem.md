# insertItems(_:beforeItem:)

**Framework**: AppKit  
**Kind**: method

Inserts the provided items immediately before the item with the specified identifier in the snapshot.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func insertItems(_ identifiers: [ItemIdentifierType], beforeItem beforeIdentifier: ItemIdentifierType)
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to add to the snapshot.
- `beforeIdentifier`: The identifier of the item before which to insert the new items.

## See Also

- [func insertItems([ItemIdentifierType], afterItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:afteritem:).md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], afterSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:aftersection:).md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], beforeSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:beforesection:).md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:beforeitem:))*