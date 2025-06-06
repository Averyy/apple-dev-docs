# pointerInteraction(_:regionFor:defaultRegion:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a region as the pointer moves within the interaction’s view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pointerInteraction(_ interaction: UIPointerInteraction, regionFor request: UIPointerRegionRequest, defaultRegion: UIPointerRegion) -> UIPointerRegion?
```

#### Return Value

A `UIPointerRegion` in which to apply a pointer style. Return `nil` to indicate that this interaction typically doesn’t customize the pointer for the current location.

## Parameters

- `interaction`: This  .
- `request`: The   that describes the pointer’s location in the interaction’s view.
- `defaultRegion`: The   that represents the entire surface of the interaction’s view.

## See Also

- [func pointerInteraction(UIPointerInteraction, styleFor: UIPointerRegion) -> UIPointerStyle?](uipointerinteractiondelegate/pointerinteraction(_:stylefor:).md)
  Asks the delegate for a pointer style after an interaction receives a new region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:regionfor:defaultregion:))*