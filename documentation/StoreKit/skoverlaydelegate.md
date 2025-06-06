# SKOverlayDelegate

**Framework**: StoreKit  
**Kind**: protocol

Methods for responding to the overlay’s appearance, dismissal, or failure to load.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol SKOverlayDelegate : NSObjectProtocol
```

## Topics

### Responding to the Overlay’s Appearance and Disappearance
- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:).md)
  Indicates that the platform presents an overlay.
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:).md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:).md)
  Indicates that the platform dismisses an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:).md)
  Indicates that platform finished dismissing an overlay.
- [SKOverlay.TransitionContext](skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.
### Responding to Failures
- [func storeOverlayDidFailToLoad(SKOverlay, error: any Error)](skoverlaydelegate/storeoverlaydidfailtoload(_:error:).md)
  Indicates that an overlay failed to load.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any SKOverlayDelegate)?](skoverlay/delegate.md)
  The overlay’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate)*