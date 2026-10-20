# ignore(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the gesture recognizer to ignore a specific press of the given event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func ignore(_ button: UIPress, for event: UIPressesEvent)
```

```objc
- (void) ignorePress:(UIPress *) button forEvent:(UIPressesEvent *) event;
```

#### Discussion

If a button press isn’t part of this gesture you may pass it to this method, causing it to be ignored. `UIGestureRecognizer` does not cancel ignored presses on the associated view even if [`cancelsTouchesInView`](./cancelstouchesinview.md) is [`true`](../../Swift/true.md). This method is intended to be called, not overridden.

## Parameters

- `button`: A [`UIButton`](../uibutton.md) object that is part of the current button press event and associated with `event`.
- `event`: A [`UIEvent`](../uievent.md) object that includes a reference to `touch`.

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
- [func pressesBegan(Set<UIPress>, with: UIPressesEvent)](./pressesbegan%28_,with%29.md)
  Sent to the receiver when a physical button is pressed in the associated view.
- [func pressesChanged(Set<UIPress>, with: UIPressesEvent)](./presseschanged%28_,with%29.md)
  Sent to the receiver when the [`force`](../uipress/force.md) of the press has changed in the associated view.
- [func pressesEnded(Set<UIPress>, with: UIPressesEvent)](./pressesended%28_,with%29.md)
  Sent to the receiver when a button is released from the associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/ignore(_:for:)-8qqor)*