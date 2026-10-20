# storeOverlayDidFinishDismissal(_:transitionContext:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Indicates that platform finished dismissing an overlay.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func storeOverlayDidFinishDismissal(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

```objc
- (void) storeOverlay:(SKOverlay *) overlay didFinishDismissal:(SKOverlayTransitionContext *) transitionContext;
```

## Parameters

- `overlay`: An app banner object that disappeared.
- `transitionContext`: The context you can use to animate changes to UI components when the overlay disappears.

## See Also

### Responding to the Overlay’s Appearance and Disappearance
- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaywillstartpresentation%28_,transitioncontext%29.md)
  Indicates that the platform presents an overlay.
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaydidfinishpresentation%28_,transitioncontext%29.md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaywillstartdismissal%28_,transitioncontext%29.md)
  Indicates that the platform dismisses an overlay.
- [SKOverlay.TransitionContext](../skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:))*