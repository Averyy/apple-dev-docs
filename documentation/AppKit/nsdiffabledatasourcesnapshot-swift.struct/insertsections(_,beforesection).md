# insertSections(_:beforeSection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided sections immediately before the section with the specified identifier in the snapshot.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func insertSections(_ identifiers: [SectionIdentifierType], beforeSection toIdentifier: SectionIdentifierType)
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the sections to add to the snapshot.
- `toIdentifier`: The identifier of the section before which to insert the new sections.

## See Also

### Inserting Items and Sections
- [func insertItems([ItemIdentifierType], afterItem: ItemIdentifierType)](./insertitems%28_,afteritem%29.md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems([ItemIdentifierType], beforeItem: ItemIdentifierType)](./insertitems%28_,beforeitem%29.md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], afterSection: SectionIdentifierType)](./insertsections%28_,aftersection%29.md)
  Inserts the provided sections immediately after the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:beforesection:))*