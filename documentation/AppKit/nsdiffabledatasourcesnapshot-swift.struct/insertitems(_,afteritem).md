# insertItems(_:afterItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided items immediately after the item with the specified identifier in the snapshot.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func insertItems(_ identifiers: [ItemIdentifierType], afterItem afterIdentifier: ItemIdentifierType)
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to add to the snapshot.
- `afterIdentifier`: The identifier of the item after which to insert the new items.

## See Also

### Inserting Items and Sections
- [func insertItems([ItemIdentifierType], beforeItem: ItemIdentifierType)](./insertitems%28_,beforeitem%29.md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], afterSection: SectionIdentifierType)](./insertsections%28_,aftersection%29.md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], beforeSection: SectionIdentifierType)](./insertsections%28_,beforesection%29.md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:afteritem:))*