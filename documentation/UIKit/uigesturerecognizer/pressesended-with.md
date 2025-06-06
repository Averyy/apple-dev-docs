# pressesEnded(_:with:)

**Framework**: UIKit  
**Kind**: method

Sent to the receiver when a button is released from the associated view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent)
```

#### Discussion

This method has the same signature as the corresponding one declared by [`UIResponder`](uiresponder.md). With this method, a gesture recognizer receives press objects (in their [`UIPress.Phase.ended`](uipress/phase-swift.enum/ended.md) phase) before the view attached to the gesture recognizer receives them. `UIGestureRecognizer` objects are not in the responder chain, yet they observe presses hit-tested to their view and their view’s subviews.

If the gesture recognizer is interpreting a continuous gesture, it should set its state to [`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md) upon receiving this message. If at any point in its handling of the press objects the gesture recognizer determines that the press event sequence is not its gesture, it should set its state to [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md).

## Parameters

- `presses`: A set of   instances in the event represented by   that represent the touches in the   phase.
- `event`: A   object that includes a reference to  .

## See Also

- [func touchesBegan(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchesbegan(_:with:).md)
  Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [func touchesMoved(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchesmoved(_:with:).md)
  Sent to the gesture recognizer when one or more fingers move in the associated view.
- [func touchesEnded(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchesended(_:with:).md)
  Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [func touchesCancelled(Set<UITouch>, with: UIEvent)](uigesturerecognizer/touchescancelled(_:with:).md)
  Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [func touchesEstimatedPropertiesUpdated(Set<UITouch>)](uigesturerecognizer/touchesestimatedpropertiesupdated(_:).md)
  Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
- [func reset()](uigesturerecognizer/reset.md)
  Overridden to reset internal state when a gesture recognition attempt completes.
- [func ignore(UITouch, for: UIEvent)](uigesturerecognizer/ignore(_:for:)-5f685.md)
  Tells the gesture recognizer to ignore a specific touch of the given event.
- [func canBePrevented(by: UIGestureRecognizer) -> Bool](uigesturerecognizer/canbeprevented(by:).md)
  Overridden to indicate that the specified gesture recognizer can prevent the receiver from recognizing a gesture.
- [func canPrevent(UIGestureRecognizer) -> Bool](uigesturerecognizer/canprevent(_:).md)
  Overridden to indicate that the receiver can prevent the specified gesture recognizer from recognizing its gesture.
- [func shouldReceive(UIEvent) -> Bool](uigesturerecognizer/shouldreceive(_:).md)
- [func shouldRequireFailure(of: UIGestureRecognizer) -> Bool](uigesturerecognizer/shouldrequirefailure(of:).md)
  Overridden to indicate that the receiver requires the specified gesture recognizer to fail.
- [func shouldBeRequiredToFail(by: UIGestureRecognizer) -> Bool](uigesturerecognizer/shouldberequiredtofail(by:).md)
  Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [func ignore(UIPress, for: UIPressesEvent)](uigesturerecognizer/ignore(_:for:)-8qqor.md)
  Tells the gesture recognizer to ignore a specific press of the given event.
- [func pressesBegan(Set<UIPress>, with: UIPressesEvent)](uigesturerecognizer/pressesbegan(_:with:).md)
  Sent to the receiver when a physical button is pressed in the associated view.
- [func pressesChanged(Set<UIPress>, with: UIPressesEvent)](uigesturerecognizer/presseschanged(_:with:).md)
  Sent to the receiver when the [`force`](uipress/force.md) of the press has changed in the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/pressesended(_:with:))*