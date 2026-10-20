# pointerInteraction(_:willEnter:animator:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when the pointer enters a given region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
optional func pointerInteraction(_ interaction: UIPointerInteraction, willEnter region: UIPointerRegion, animator: any UIPointerInteractionAnimating)
```

```objc
- (void) pointerInteraction:(UIPointerInteraction *) interaction willEnterRegion:(UIPointerRegion *) region animator:(id<UIPointerInteractionAnimating>) animator;
```

## Parameters

- `interaction`: This [`UIPointerInteraction`](../uipointerinteraction.md).
- `region`: The [`UIPointerRegion`](../uipointerregion.md) that represents the entire surface of the interaction’s view.
- `animator`: The animator the framework runs when the pointer enters the region. Add animations to run them alongside the pointer’s entrance animation.

## See Also

### Handling animations for pointer regions
- [func pointerInteraction(UIPointerInteraction, willExit: UIPointerRegion, animator: any UIPointerInteractionAnimating)](./pointerinteraction%28_,willexit,animator%29.md)
  Informs the delegate when the pointer exits a given region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:willenter:animator:))*