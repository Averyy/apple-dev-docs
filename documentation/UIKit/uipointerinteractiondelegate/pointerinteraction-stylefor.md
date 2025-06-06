# pointerInteraction(_:styleFor:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a pointer style after an interaction receives a new region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pointerInteraction(_ interaction: UIPointerInteraction, styleFor region: UIPointerRegion) -> UIPointerStyle?
```

#### Return Value

A `UIPointerStyle` describing the desired hover effect or pointer appearance for the given `UIPointerRegion`.

## Parameters

- `interaction`: This  .
- `region`: The   that represents the entire surface of the interaction’s view.

## See Also

- [func pointerInteraction(UIPointerInteraction, regionFor: UIPointerRegionRequest, defaultRegion: UIPointerRegion) -> UIPointerRegion?](uipointerinteractiondelegate/pointerinteraction(_:regionfor:defaultregion:).md)
  Asks the delegate for a region as the pointer moves within the interaction’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:stylefor:))*