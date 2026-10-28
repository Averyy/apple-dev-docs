# reset()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Overridden to reset internal state when a gesture recognition attempt completes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func reset()
```

```objc
- (void) reset;
```

## Mentions

- [About the Gesture Recognizer State Machine](../about-the-gesture-recognizer-state-machine.md)
- [Implementing a Continuous Gesture Recognizer](../implementing-a-continuous-gesture-recognizer.md)
- [Implementing a discrete gesture recognizer](../implementing-a-discrete-gesture-recognizer.md)

## Discussion

The runtime calls this method after the gesture-recognizer state has been set to [`UIGestureRecognizer.State.ended`](./state-swift.enum/ended.md), [`recognized`](./state-swift.enum/recognized.md), [`UIGestureRecognizer.State.cancelled`](./state-swift.enum/cancelled.md), or [`UIGestureRecognizer.State.failed`](./state-swift.enum/failed.md)—in other words, any of the terminal states for a gesture recognition attempt. Subclasses should reset any internal state in preparation for a new attempt at gesture recognition. After this method is called, the gesture recognizer receives no further updates for touches that have begun but haven’t ended.

## See Also

### Related Documentation
- [var state: UIGestureRecognizer.State](./state-swift.property.md)
  The current state of the gesture recognizer.
### Implementing subclasses
- [func touchesBegan(Set<UITouch>, with: UIEvent)](./touchesbegan%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [func touchesMoved(Set<UITouch>, with: UIEvent)](./touchesmoved%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers move in the associated view.
- [func touchesEnded(Set<UITouch>, with: UIEvent)](./touchesended%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [func touchesCancelled(Set<UITouch>, with: UIEvent)](./touchescancelled%28_,with%29.md)
  Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [func touchesEstimatedPropertiesUpdated(Set<UITouch>)](./touchesestimatedpropertiesupdated%28_%29.md)
  Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
- [func ignore(UITouch, for: UIEvent)](./ignore%28_,for%29-5f685.md)
  Tells the gesture recognizer to ignore a specific touch of the given event.
- [func canBePrevented(by: UIGestureRecognizer) -> Bool](./canbeprevented%28by%29.md)
  Overridden to indicate that the specified gesture recognizer can prevent the receiver from recognizing a gesture.
- [func canPrevent(UIGestureRecognizer) -> Bool](./canprevent%28_%29.md)
  Overridden to indicate that the receiver can prevent the specified gesture recognizer from recognizing its gesture.
- [func shouldReceive(UIEvent) -> Bool](./shouldreceive%28_%29.md)
- [func shouldRequireFailure(of: UIGestureRecognizer) -> Bool](./shouldrequirefailure%28of%29.md)
  Overridden to indicate that the receiver requires the specified gesture recognizer to fail.
- [func shouldBeRequiredToFail(by: UIGestureRecognizer) -> Bool](./shouldberequiredtofail%28by%29.md)
  Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [func ignore(UIPress, for: UIPressesEvent)](./ignore%28_,for%29-8qqor.md)
  Tells the gesture recognizer to ignore a specific press of the given event.
- [func pressesBegan(Set<UIPress>, with: UIPressesEvent)](./pressesbegan%28_,with%29.md)
  Sent to the receiver when a physical button is pressed in the associated view.
- [func pressesChanged(Set<UIPress>, with: UIPressesEvent)](./presseschanged%28_,with%29.md)
  Sent to the receiver when the [`force`](../uipress/force.md) of the press has changed in the associated view.
- [func pressesEnded(Set<UIPress>, with: UIPressesEvent)](./pressesended%28_,with%29.md)
  Sent to the receiver when a button is released from the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/reset())*