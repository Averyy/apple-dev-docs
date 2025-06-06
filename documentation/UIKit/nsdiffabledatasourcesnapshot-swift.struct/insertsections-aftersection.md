# insertSections(_:afterSection:)

**Framework**: UIKit  
**Kind**: method

Inserts the provided sections immediately after the section with the specified identifier in the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
mutating func insertSections(_ identifiers: [SectionIdentifierType], afterSection toIdentifier: SectionIdentifierType)
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the sections to add to the snapshot.
- `toIdentifier`: The identifier of the section after which to insert the new sections.

## See Also

- [func insertItems([ItemIdentifierType], afterItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:afteritem:).md)
  Inserts the provided items immediately after the item with the specified identifier in the snapshot.
- [func insertItems([ItemIdentifierType], beforeItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertitems(_:beforeitem:).md)
  Inserts the provided items immediately before the item with the specified identifier in the snapshot.
- [func insertSections([SectionIdentifierType], beforeSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:beforesection:).md)
  Inserts the provided sections immediately before the section with the specified identifier in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/insertsections(_:aftersection:))*