# finish()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the system that user interactions signaled the completion of the transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func finish()
```

```objc
- (void) finishInteractiveTransition;
```

## Discussion

This is a convenience method that calls through to the [`finishInteractiveTransition()`](../uiviewcontrollercontexttransitioning/finishinteractivetransition%28%29.md) method of the context object.

While tracking user interactions, your gesture recognizer or event-handling code should call this methods when the interactions suggest that the transition is now complete. For example, if the user swipes a finger, and the touch events indicate that the swipe distance crossed the threshold needed to complete the gesture, call this method when the corresponding touch events end to let the system know that it can now complete the transition.

## See Also

### Managing a transition
- [func update(CGFloat)](./update%28_%29.md)
  Updates the completion percentage of the transition.
- [func pause()](./pause%28%29.md)
  Pauses an interruptible transition animation.
- [func cancel()](./cancel%28%29.md)
  Notifies the system that user interactions canceled the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/finish())*