# moveSection(withIdentifier:beforeSectionWithIdentifier:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Moves the section from its current position in the snapshot to the position immediately before the specified section.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func moveSection(withIdentifier fromSectionIdentifier: Any, beforeSectionWithIdentifier toSectionIdentifier: Any)
```

```objc
- (void) moveSectionWithIdentifier:(SectionIdentifierType) fromSectionIdentifier beforeSectionWithIdentifier:(SectionIdentifierType) toSectionIdentifier;
```

## Parameters

- `fromSectionIdentifier`: The identifier of the section to move in the snapshot.
- `toSectionIdentifier`: The identifier of the section before which to move the specified section.

## See Also

### Reordering items and sections
- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](./moveitem%28withidentifier,afteritemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(withIdentifier: Any, beforeItemWithIdentifier: Any)](./moveitem%28withidentifier,beforeitemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(withIdentifier: Any, afterSectionWithIdentifier: Any)](./movesection%28withidentifier,aftersectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately after the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/movesection(withidentifier:beforesectionwithidentifier:))*