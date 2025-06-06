# moveSection(_:beforeSection:)

**Framework**: UIKit  
**Kind**: method

Moves the section from its current position in the snapshot to the position immediately before the specified section.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
mutating func moveSection(_ identifier: SectionIdentifierType, beforeSection toIdentifier: SectionIdentifierType)
```

## Parameters

- `identifier`: The identifier of the section to move in the snapshot.
- `toIdentifier`: The identifier of the section before which to move the specified section.

## See Also

- [func moveItem(ItemIdentifierType, afterItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:afteritem:).md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(ItemIdentifierType, beforeItem: ItemIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/moveitem(_:beforeitem:).md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(SectionIdentifierType, afterSection: SectionIdentifierType)](nsdiffabledatasourcesnapshot-swift.struct/movesection(_:aftersection:).md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshot-swift.struct/movesection(_:beforesection:))*