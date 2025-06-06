# moveItem(_:afterItem:)

**Framework**: AppKit  
**Kind**: method

Moves the item from its current position in the snapshot to the position immediately after the specified item.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func moveItem(_ identifier: ItemIdentifierType, afterItem toIdentifier: ItemIdentifierType)
```

## Parameters

- `identifier`: The identifier of the item to move in the snapshot.
- `toIdentifier`: The identifier of the item after which to move the specified item.

## See Also

- [func moveItem(ItemIdentifierType, beforeItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:beforeitem:).md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(SectionIdentifierType, afterSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/movesection(_:aftersection:).md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(SectionIdentifierType, beforeSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/movesection(_:beforesection:).md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:afteritem:))*