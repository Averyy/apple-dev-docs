# storeOverlayDidFinishDismissal(_:transitionContext:)

**Framework**: StoreKit  
**Kind**: method

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

## Parameters

- `overlay`: An app banner object that disappeared.
- `transitionContext`: The context you can use to animate changes to UI components when the overlay disappears.

## See Also

- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:).md)
  Indicates that the platform presents an overlay.
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:).md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:).md)
  Indicates that the platform dismisses an overlay.
- [SKOverlay.TransitionContext](skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:))*