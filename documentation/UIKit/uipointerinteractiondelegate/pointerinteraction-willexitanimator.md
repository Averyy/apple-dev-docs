# pointerInteraction(_:willExit:animator:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when the pointer exits a given region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func pointerInteraction(_ interaction: UIPointerInteraction, willExit region: UIPointerRegion, animator: any UIPointerInteractionAnimating)
```

## Parameters

- `interaction`: This  .
- `region`: The   that represents the entire surface of the interaction’s view.
- `animator`: The animator the framework runs when the pointer exists the region. Add animations to run them alongside the pointer’s exit animation.

## See Also

- [func pointerInteraction(UIPointerInteraction, willEnter: UIPointerRegion, animator: any UIPointerInteractionAnimating)](uipointerinteractiondelegate/pointerinteraction(_:willenter:animator:).md)
  Informs the delegate when the pointer enters a given region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:willexit:animator:))*