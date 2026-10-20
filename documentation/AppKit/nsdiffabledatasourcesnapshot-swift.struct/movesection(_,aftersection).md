# moveSection(_:afterSection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the section from its current position in the snapshot to the position immediately after the specified section.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func moveSection(_ identifier: SectionIdentifierType, afterSection toIdentifier: SectionIdentifierType)
```

## Parameters

- `identifier`: The identifier of the section to move in the snapshot.
- `toIdentifier`: The identifier of the section after which to move the specified section.

## See Also

### Reordering Items and Sections
- [func moveItem(ItemIdentifierType, afterItem: ItemIdentifierType)](./moveitem%28_,afteritem%29.md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(ItemIdentifierType, beforeItem: ItemIdentifierType)](./moveitem%28_,beforeitem%29.md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(SectionIdentifierType, beforeSection: SectionIdentifierType)](./movesection%28_,beforesection%29.md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/movesection(_:aftersection:))*