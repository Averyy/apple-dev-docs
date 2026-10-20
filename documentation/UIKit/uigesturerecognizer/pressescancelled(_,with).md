# pressesCancelled(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the receiver when a system event (such as a low-memory warning) cancels a press event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func pressesCancelled(_ presses: Set<UIPress>, with event: UIPressesEvent)
```

```objc
- (void) pressesCancelled:(NSSet<UIPress *> *) presses withEvent:(UIPressesEvent *) event;
```

## Mentions

- [About the Gesture Recognizer State Machine](../about-the-gesture-recognizer-state-machine.md)

#### Discussion

This method has the same signature as the corresponding one declared by [`UIResponder`](../uiresponder.md). With this method a gesture recognizer receives press objects (in their [`UIPress.Phase.cancelled`](../uipress/phase-swift.enum/cancelled.md) phase) before the view attached to the gesture recognizer receives them. `UIGestureRecognizer` objects are not in the responder chain, yet they observe presses hit-tested to their view and their view’s subviews.

If the gesture recognizer is interpreting a continuous gesture, it should set its state to [`UIGestureRecognizer.State.began`](./state-swift.enum/began.md) upon receiving this message. If at any point in its handling of the press objects the gesture recognizer determines that the press event sequence is not its gesture, it should set its state to [`UIGestureRecognizer.State.cancelled`](./state-swift.enum/cancelled.md).

## Parameters

- `presses`: A set of [`UIPress`](../uipress.md) instances in the event represented by `event` that represent the touches in the [`UIPress.Phase.cancelled`](../uipress/phase-swift.enum/cancelled.md) phase.
- `event`: A [`UIEvent`](../uievent.md) object that includes a reference to `press`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/pressescancelled(_:with:))*