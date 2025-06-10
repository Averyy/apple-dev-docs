# moveSection(withIdentifier:beforeSectionWithIdentifier:)

**Framework**: AppKit  
**Kind**: method

Moves the section from its current position in the snapshot to the position immediately before the specified section.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func moveSection(withIdentifier fromSectionIdentifier: Any, beforeSectionWithIdentifier toSectionIdentifier: Any)
```

## Parameters

- `fromSectionIdentifier`: The identifier of the section to move in the snapshot.
- `toSectionIdentifier`: The identifier of the section before which to move the specified section.

## See Also

- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:).md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(withIdentifier: Any, beforeItemWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:beforeitemwithidentifier:).md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(withIdentifier: Any, afterSectionWithIdentifier: Any)](nsdiffabledatasourcesnapshotreference/movesection(withidentifier:aftersectionwithidentifier:).md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/movesection(withidentifier:beforesectionwithidentifier:))*