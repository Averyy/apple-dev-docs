# SKOverlay.TransitionContext

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

A context object you can use to animate UI changes while the platform presents or dismisses an overlay.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class TransitionContext
```

```objc
@interface SKOverlayTransitionContext : NSObject
```

## Overview

For more information on animating UI changes while the system presents or dismisses an overlay, see [`storeOverlayWillStartPresentation(_:transitionContext:)`](../skoverlaydelegate/storeoverlaywillstartpresentation%28_,transitioncontext%29.md) and [`storeOverlayWillStartDismissal(_:transitionContext:)`](../skoverlaydelegate/storeoverlaywillstartdismissal%28_,transitioncontext%29.md).

## Topics

### Adding an Animation
- [func addAnimation(() -> Void)](./transitioncontext/addanimation%28_%29.md)
  Adds a closure you can use to animate view properties.
- [var startFrame: CGRect](./transitioncontext/startframe.md)
  The size and location of the overlay before the transition.
- [var endFrame: CGRect](./transitioncontext/endframe.md)
  The size and location of the overlay at the end of the transition.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to the Overlay’s Appearance and Disappearance
- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](../skoverlaydelegate/storeoverlaywillstartpresentation%28_,transitioncontext%29.md)
  Indicates that the platform presents an overlay.
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](../skoverlaydelegate/storeoverlaydidfinishpresentation%28_,transitioncontext%29.md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](../skoverlaydelegate/storeoverlaywillstartdismissal%28_,transitioncontext%29.md)
  Indicates that the platform dismisses an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](../skoverlaydelegate/storeoverlaydidfinishdismissal%28_,transitioncontext%29.md)
  Indicates that platform finished dismissing an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/transitioncontext)*