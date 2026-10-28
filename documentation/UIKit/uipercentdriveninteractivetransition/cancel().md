# cancel()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the system that user interactions canceled the transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancelInteractiveTransition;
```

## Discussion

This is a convenience method that calls through to the [`cancelInteractiveTransition()`](../uiviewcontrollercontexttransitioning/cancelinteractivetransition%28%29.md) method of the context object.

While tracking user interactions, your gesture recognizer or event-handling code would call this method when interactions suggest that the user wants to cancel or abort the view controller transition. For example, if the user reverses the swipe direction and then touch events end, suggesting that the user decided against the transition, you would call this method.

## See Also

### Managing a transition
- [func update(CGFloat)](./update%28_%29.md)
  Updates the completion percentage of the transition.
- [func pause()](./pause%28%29.md)
  Pauses an interruptible transition animation.
- [func finish()](./finish%28%29.md)
  Notifies the system that user interactions signaled the completion of the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipercentdriveninteractivetransition/cancel())*