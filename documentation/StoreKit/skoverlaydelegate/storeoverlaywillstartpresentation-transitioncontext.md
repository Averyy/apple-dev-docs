# storeOverlayWillStartPresentation(_:transitionContext:)

**Framework**: StoreKit  
**Kind**: method

Indicates that the platform presents an overlay.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func storeOverlayWillStartPresentation(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

#### Discussion

Use the `transitionContext` parameter to animate updates to the UI on the main thread. For example, make a [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView) disappear by animating the change of its opacity to 0% as shown in the following code:

```swift
func storeOverlayWillStartPresentation(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext) {
    transitionContext.addAnimation { [self] in
        self.imageView.layer.opacity = 0
    }
}
```

## Parameters

- `overlay`: An overlay object that’s about to appear.
- `transitionContext`: A context you can use to animate changes to UI components as the overlay appears.

## See Also

- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:).md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:).md)
  Indicates that the platform dismisses an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:).md)
  Indicates that platform finished dismissing an overlay.
- [SKOverlay.TransitionContext](skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:))*