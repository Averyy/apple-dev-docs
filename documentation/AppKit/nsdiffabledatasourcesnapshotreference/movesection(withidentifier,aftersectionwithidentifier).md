# moveSection(withIdentifier:afterSectionWithIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the section from its current position in the snapshot to the position immediately after the specified section.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func moveSection(withIdentifier fromSectionIdentifier: Any, afterSectionWithIdentifier toSectionIdentifier: Any)
```

```objc
- (void) moveSectionWithIdentifier:(SectionIdentifierType) fromSectionIdentifier afterSectionWithIdentifier:(SectionIdentifierType) toSectionIdentifier;
```

## Parameters

- `fromSectionIdentifier`: The identifier of the section to move in the snapshot.
- `toSectionIdentifier`: The identifier of the section after which to move the specified section.

## See Also

### Reordering items and sections
- [func moveItem(withIdentifier: Any, afterItemWithIdentifier: Any)](./moveitem%28withidentifier,afteritemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately after the specified item.
- [func moveItem(withIdentifier: Any, beforeItemWithIdentifier: Any)](./moveitem%28withidentifier,beforeitemwithidentifier%29.md)
  Moves the item from its current position in the snapshot to the position immediately before the specified item.
- [func moveSection(withIdentifier: Any, beforeSectionWithIdentifier: Any)](./movesection%28withidentifier,beforesectionwithidentifier%29.md)
  Moves the section from its current position in the snapshot to the position immediately before the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/movesection(withidentifier:aftersectionwithidentifier:))*