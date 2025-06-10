# reset()

**Framework**: UIKit  
**Kind**: method

Overridden to reset internal state when a gesture recognition attempt completes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func reset()
```

## Mentions

- [About the Gesture Recognizer State Machine](about-the-gesture-recognizer-state-machine.md)
- [Implementing a Discrete Gesture Recognizer](implementing-a-discrete-gesture-recognizer.md)
- [Implementing a Continuous Gesture Recognizer](implementing-a-continuous-gesture-recognizer.md)

#### Discussion

The runtime calls this method after the gesture-recognizer state has been set to [`UIGestureRecognizer.State.ended`](uigesturerecognizer/state-swift.enum/ended.md), [`recognized`](uigesturerecognizer/state-swift.enum/recognized.md), [`UIGestureRecognizer.State.cancelled`](uigesturerecognizer/state-swift.enum/cancelled.md), or [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md)—in other words, any of the terminal states for a gesture recognition attempt. Subclasses should reset any internal state in preparation for a new attempt at gesture recognition. After this method is called, the gesture recognizer receives no further updates for touches that have begun but haven’t ended.

## See Also

- [var state: UIGestureRecognizer.State](uigesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
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
- [func pressesEnded(Set<UIPress>, with: UIPressesEvent)](uigesturerecognizer/pressesended(_:with:).md)
  Sent to the receiver when a button is released from the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/reset())*