# touchesCancelled(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent)
```

```objc
- (void) touchesCancelled:(NSSet<UITouch *> *) touches withEvent:(UIEvent *) event;
```

#### Discussion

This method has the same exact signature as the corresponding one declared by [`UIResponder`](../uiresponder.md). Through this method a gesture recognizer receives touch objects (in their [`UITouch.Phase.cancelled`](../uitouch/phase-swift.enum/cancelled.md) phase) before the view attached to the gesture recognizer receives them. `UIGestureRecognizer` objects are not in the responder chain, yet observe touches hit-tested to their view and their view’s subviews. After observation, the delivery of touch objects to the attached view, or their disposition otherwise, is affected by the [`cancelsTouchesInView`](./cancelstouchesinview.md), [`delaysTouchesBegan`](./delaystouchesbegan.md), and [`delaysTouchesEnded`](./delaystouchesended.md) properties.

Upon receiving this message, the gesture recognizer for a continuous gesture should set its state to [`UIGestureRecognizer.State.cancelled`](./state-swift.enum/cancelled.md); a gesture recognizer for a discrete gesture should set its state to [`UIGestureRecognizer.State.failed`](./state-swift.enum/failed.md).

## Parameters

- `touches`: A set of [`UITouch`](../uitouch.md) instances in the event represented by `event` that represent the touches in the [`UITouch.Phase.cancelled`](../uitouch/phase-swift.enum/cancelled.md) phase.
- `event`: A [`UIEvent`](../uievent.md) object representing the event to which the touches belong.

## See Also

### Implementing subclasses
- [func touchesBegan(Set<UITouch>, with: UIEvent)](./touchesbegan%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [func touchesMoved(Set<UITouch>, with: UIEvent)](./touchesmoved%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers move in the associated view.
- [func touchesEnded(Set<UITouch>, with: UIEvent)](./touchesended%28_,with%29.md)
  Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [func touchesEstimatedPropertiesUpdated(Set<UITouch>)](./touchesestimatedpropertiesupdated%28_%29.md)
  Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
- [func reset()](./reset%28%29.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/touchescancelled(_:with:))*