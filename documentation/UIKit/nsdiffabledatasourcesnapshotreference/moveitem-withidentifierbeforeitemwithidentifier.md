# moveItem(withIdentifier:beforeItemWithIdentifier:)

**Framework**: UIKit  
**Kind**: method

Moves the item from its current position in the snapshot to the position immediately before the specified item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func moveItem(withIdentifier fromIdentifier: Any, beforeItemWithIdentifier toIdentifier: Any)
```

## Parameters

- `fromIdentifier`: The identifier of the item to move in the snapshot.
- `toIdentifier`: The identifier of the item before which to move the specified item.

## See Also

- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:).md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveSection(withIdentifier: Any, afterSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/movesection(withidentifier:aftersectionwithidentifier:).md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(withIdentifier: Any, beforeSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/movesection(withidentifier:beforesectionwithidentifier:).md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:beforeitemwithidentifier:))*