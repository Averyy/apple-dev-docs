# moveItem(_:beforeItem:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Moves the item from its current position in the snapshot to the position immediately before the specified item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS

## Declaration

```swift
mutating func moveItem(_ identifier: ItemIdentifierType, beforeItem toIdentifier: ItemIdentifierType)
```

## Parameters

- `identifier`: The identifier of the item to move in the snapshot.
- `toIdentifier`: The identifier of the item before which to move the specified item.

## See Also

### Reordering items and sections
- [func moveItem(ItemIdentifierType, afterItem: ItemIdentifierType)](./moveitem%28_,afteritem%29.md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveSection(SectionIdentifierType, afterSection: SectionIdentifierType)](./movesection%28_,aftersection%29.md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(SectionIdentifierType, beforeSection: SectionIdentifierType)](./movesection%28_,beforesection%29.md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:beforeitem:))*