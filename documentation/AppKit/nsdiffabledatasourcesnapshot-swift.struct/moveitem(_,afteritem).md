# moveItem(_:afterItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

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

### Reordering Items and Sections
- [func moveItem(ItemIdentifierType, beforeItem: ItemIdentifierType)](./moveitem%28_,beforeitem%29.md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(SectionIdentifierType, afterSection: SectionIdentifierType)](./movesection%28_,aftersection%29.md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(SectionIdentifierType, beforeSection: SectionIdentifierType)](./movesection%28_,beforesection%29.md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:afteritem:))*