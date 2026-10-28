# dragInteraction(_:item:willAnimateCancelWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the system’s cancellation animation is about to start.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, item: UIDragItem, willAnimateCancelWith animator: any UIDragAnimating)
```

```objc
- (void) dragInteraction:(UIDragInteraction *) interaction item:(UIDragItem *) item willAnimateCancelWithAnimator:(id<UIDragAnimating>) animator;
```

## Discussion

This method is called for each drag item, whether it is visible or not.

To add a custom animation block that runs during the cancellation animation, pass the block to the animator’s [`addAnimations(_:)`](../uidraganimating/addanimations%28_%29.md) method.

To add a completion block that runs after the cancellation animation has finished, pass the block to the animator’s [`addCompletion(_:)`](../uidraganimating/addcompletion%28_%29.md) method.

## Parameters

- `interaction`: The interaction that called this method.
- `item`: The current drag item.
- `animator`: The animator that provides custom animations to run alongside the system’s animation. You can also use it to add a completion block that runs after the animations have finished.

## See Also

### Animating the drag behaviors
- [func dragInteraction(UIDragInteraction, willAnimateLiftWith: any UIDragAnimating, session: any UIDragSession)](./draginteraction%28_,willanimateliftwith,session%29.md)
  Tells the delegate the system’s lift animation is about to start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:item:willanimatecancelwith:))*