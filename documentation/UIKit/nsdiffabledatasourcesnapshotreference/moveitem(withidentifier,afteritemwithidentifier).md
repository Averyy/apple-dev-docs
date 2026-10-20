# moveItem(withIdentifier:afterItemWithIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Moves the item from its current position in the snapshot to the position immediately after the specified item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/moveitem(withidentifier:afteritemwithidentifier:))*