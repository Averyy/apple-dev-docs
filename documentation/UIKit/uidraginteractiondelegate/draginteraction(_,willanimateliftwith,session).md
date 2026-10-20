# dragInteraction(_:willAnimateLiftWith:session:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the system’s lift animation is about to start.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, willAnimateLiftWith animator: any UIDragAnimating, session: any UIDragSession)
```

```objc
- (void) dragInteraction:(UIDragInteraction *) interaction willAnimateLiftWithAnimator:(id<UIDragAnimating>) animator session:(id<UIDragSession>) session;
```

#### Discussion

To add a custom animation block that runs during the lift animation, pass the block to the animator’s [`addAnimations(_:)`](../uidraganimating/addanimations%28_%29.md) method.

To add a completion block that runs after the lift animation has finished, pass the block to the animator’s [`addCompletion(_:)`](../uidraganimating/addcompletion%28_%29.md) method.

## Parameters

- `interaction`: The interaction that called this method.
- `animator`: The animator that provides custom animations to run alongside the system’s lift animation. You can also use it to add a completion block that runs after the animations have finished.
- `session`: The current drag session.

## See Also

### Animating the drag behaviors
- [func dragInteraction(UIDragInteraction, item: UIDragItem, willAnimateCancelWith: any UIDragAnimating)](./draginteraction%28_,item,willanimatecancelwith%29.md)
  Tells the delegate the system’s cancellation animation is about to start.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:willanimateliftwith:session:))*