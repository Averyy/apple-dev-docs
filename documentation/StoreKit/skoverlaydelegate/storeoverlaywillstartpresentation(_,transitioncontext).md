# storeOverlayWillStartPresentation(_:transitionContext:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) storeOverlay:(SKOverlay *) overlay willStartPresentation:(SKOverlayTransitionContext *) transitionContext;
```

#### Discussion

Use the `transitionContext` parameter to animate updates to the UI on the main thread. For example, make a [`UIImageView`](../../UIKit/uiimageview.md) disappear by animating the change of its opacity to 0% as shown in the following code:

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

### Responding to the Overlay’s Appearance and Disappearance
- [func storeOverlayDidFinishPresentation(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaydidfinishpresentation%28_,transitioncontext%29.md)
  Indicates that the platform finished presenting an overlay.
- [func storeOverlayWillStartDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaywillstartdismissal%28_,transitioncontext%29.md)
  Indicates that the platform dismisses an overlay.
- [func storeOverlayDidFinishDismissal(SKOverlay, transitionContext: SKOverlay.TransitionContext)](./storeoverlaydidfinishdismissal%28_,transitioncontext%29.md)
  Indicates that platform finished dismissing an overlay.
- [SKOverlay.TransitionContext](../skoverlay/transitioncontext.md)
  A context object you can use to animate UI changes while the platform presents or dismisses an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlaydelegate/storeoverlaywillstartpresentation(_:transitioncontext:))*