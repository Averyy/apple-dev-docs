# moveSection(withIdentifier:afterSectionWithIdentifier:)

**Framework**: UIKit  
**Kind**: method

Moves the section from its current position in the snapshot to the position immediately after the specified section.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func moveSection(withIdentifier fromSectionIdentifier: Any, afterSectionWithIdentifier toSectionIdentifier: Any)
```

## Parameters

- `fromSectionIdentifier`: The identifier of the section to move in the snapshot.
- `toSectionIdentifier`: The identifier of the section after which to move the specified section.

## See Also

- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:).md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(withIdentifier: Any, beforeItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:beforeitemwithidentifier:).md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(withIdentifier: Any, beforeSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/movesection(withidentifier:beforesectionwithidentifier:).md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/movesection(withidentifier:aftersectionwithidentifier:))*