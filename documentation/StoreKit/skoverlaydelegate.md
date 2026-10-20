# SKOverlayDelegate

**Framework**: StoreKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol SKOverlayDelegate <NSObject>
```

## Topics

### Responding to the Overlay’s Appearance and Disappearance
- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./skoverlaydelegate/storeoverlaywillstartpresentation%28_,transitioncontext%29.md)
  Indicates that the platform presents an overlay.
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./skoverlaydelegate/storeoverlaydidfinishpresentation%28_,transitioncontext%29.md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./skoverlaydelegate/storeoverlaywillstartdismissal%28_,transitioncontext%29.md)
  Indicates that the platform dismisses an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./skoverlaydelegate/storeoverlaydidfinishdismissal%28_,transitioncontext%29.md)
  Indicates that platform finished dismissing an overlay.
- [SKOverlay.TransitionContext](./skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.
### Responding to Failures
- [func storeOverlayDidFailToLoad(SKOverlay, error: any Error)](./skoverlaydelegate/storeoverlaydidfailtoload%28_,error%29.md)
  Indicates that an overlay failed to load.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting a delegate
- [var delegate: (any SKOverlayDelegate)?](./skoverlay/delegate.md)
  The overlay’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate)*