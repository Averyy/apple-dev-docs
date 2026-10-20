# moveSection(_:beforeSection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the section from its current position in the snapshot to the position immediately before the specified section.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func moveSection(_ identifier: SectionIdentifierType, beforeSection toIdentifier: SectionIdentifierType)
```

## Parameters

- `identifier`: The identifier of the section to move in the snapshot.
- `toIdentifier`: The identifier of the section before which to move the specified section.

## See Also

### Reordering Items and Sections
- [func moveItem(ItemIdentifierType, afterItem: ItemIdentifierType)](./moveitem%28_,afteritem%29.md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(ItemIdentifierType, beforeItem: ItemIdentifierType)](./moveitem%28_,beforeitem%29.md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(SectionIdentifierType, afterSection: SectionIdentifierType)](./movesection%28_,aftersection%29.md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/movesection(_:beforesection:))*