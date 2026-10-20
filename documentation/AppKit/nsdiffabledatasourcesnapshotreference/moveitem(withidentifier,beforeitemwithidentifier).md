# moveItem(withIdentifier:beforeItemWithIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the item from its current position in the snapshot to the position immediately before the specified item.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func moveItem(withIdentifier fromIdentifier: Any, beforeItemWithIdentifier toIdentifier: Any)
```

```objc
- (void) moveItemWithIdentifier:(ItemIdentifierType) fromIdentifier beforeItemWithIdentifier:(ItemIdentifierType) toIdentifier;
```

## Parameters

- `fromIdentifier`: The identifier of the item to move in the snapshot.
- `toIdentifier`: The identifier of the item before which to move the specified item.

## See Also

### Reordering items and sections
- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](./moveitem%28withidentifier,afteritemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveSection(withIdentifier: Any, afterSectionWithIdentifier: Any)](./movesection%28withidentifier,aftersectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(withIdentifier: Any, beforeSectionWithIdentifier: Any)](./movesection%28withidentifier,beforesectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:beforeitemwithidentifier:))*