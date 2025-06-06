# storeOverlayWillStartDismissal(_:transitionContext:)

**Framework**: StoreKit  
**Kind**: method

Indicates that the platform dismisses an overlay.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func storeOverlayWillStartDismissal(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext)
```

#### Discussion

Use the `transitionContext` parameter to animate updates to the UI on the main thread. For example, make a [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView) appear by animating the change of its opacity to 100%`,` as shown in the following code:

```swift
func storeOverlayWillStartDismissal(_ overlay: SKOverlay, transitionContext: SKOverlay.TransitionContext) {
    transitionContext.addAnimation { [self] in
        self.imageView.layer.opacity = 1
    }
}
```

## Parameters

- `overlay`: An overlay object that’s about to disappear.
- `transitionContext`: The context you can use to animate changes to UI components when the overlay disappears.

## See Also

- [func storeOverlayWillStartPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:).md)
  Indicates that the platform presents an overlay.
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishpresentation(_:transitioncontext:).md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](skoverlaydelegate/storeoverlaydidfinishdismissal(_:transitioncontext:).md)
  Indicates that platform finished dismissing an overlay.
- [SKOverlay.TransitionContext](skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaywillstartdismissal(_:transitioncontext:))*