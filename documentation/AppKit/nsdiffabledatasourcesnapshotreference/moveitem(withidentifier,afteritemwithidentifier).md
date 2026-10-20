# moveItem(withIdentifier:afterItemWithIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the item from its current position in the snapshot to the position immediately after the specified item.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func moveItem(withIdentifier fromIdentifier: Any, afterItemWithIdentifier toIdentifier: Any)
```

```objc
- (void) moveItemWithIdentifier:(ItemIdentifierType) fromIdentifier afterItemWithIdentifier:(ItemIdentifierType) toIdentifier;
```

## Parameters

- `fromIdentifier`: The identifier of the item to move in the snapshot.
- `toIdentifier`: The identifier of the item after which to move the specified item.

## See Also

### Reordering items and sections
- [func moveItem(withIdentifier: Any, beforeItemWithIdentifier: Any)](./moveitem%28withidentifier,beforeitemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(withIdentifier: Any, afterSectionWithIdentifier: Any)](./movesection%28withidentifier,aftersectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.
- [func moveSection(withIdentifier: Any, beforeSectionWithIdentifier: Any)](./movesection%28withidentifier,beforesectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:))*