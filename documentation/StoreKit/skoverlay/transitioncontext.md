# SKOverlay.TransitionContext

**Framework**: StoreKit  
**Kind**: class

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

#### Overview

For more information on animating UI changes while the system presents or dismisses an overlay, see [`storeOverlayWillStartPresentation(_:transitionContext:)`](skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:).md) and [`storeOverlayWillStartDismissal(_:transitionContext:)`](skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:).md).

## Topics

### Adding an Animation
- [func addAnimation(() -> Void)](skoverlay/transitioncontext/addanimation(_:).md)
  Adds a closure you can use to animate view properties.
- [var startFrame: CGRect](skoverlay/transitioncontext/startframe.md)
  The size and location of the overlay before the transition.
- [var endFrame: CGRect](skoverlay/transitioncontext/endframe.md)
  The size and location of the overlay at the end of the transition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:).md)
  Indicates that the platform presents an overlay.
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:).md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:).md)
  Indicates that the platform dismisses an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:).md)
  Indicates that platform finished dismissing an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/transitioncontext)*