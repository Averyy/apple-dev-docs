# storeOverlayDidFinishPresentation(_:transitionContext:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Indicates that the platform finished presenting an overlay.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func storeOverlayDidFinishPresentation(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

```objc
- (void) storeOverlay:(SKOverlay *) overlay didFinishPresentation:(SKOverlayTransitionContext *) transitionContext;
```

## Parameters

- `overlay`: The overlay object that appears.
- `transitionContext`: A context you can use to animate changes to UI components after the overlay appears.

## See Also

### Responding to the Overlay’s Appearance and Disappearance
- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaywillstartpresentation%28_,transitioncontext%29.md)
  Indicates that the platform presents an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaywillstartdismissal%28_,transitioncontext%29.md)
  Indicates that the platform dismisses an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaydidfinishdismissal%28_,transitioncontext%29.md)
  Indicates that platform finished dismissing an overlay.
- [SKOverlay.TransitionContext](../skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:))*