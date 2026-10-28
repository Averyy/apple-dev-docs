# ignore(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the gesture recognizer to ignore a specific touch of the given event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
func ignore(_ touch: UITouch, for event: UIEvent)
```

```objc
- (void) ignoreTouch:(UITouch *) touch forEvent:(UIEvent *) event;
```

## Discussion

If a touch isn’t part of this gesture you may pass it to this method, causing it to be ignored. `UIGestureRecognizer` does not cancel ignored touches on the associated view. This method is intended to be called, not overridden.

## Parameters

- `touch`: A [`UITouch`](../uitouch.md) object that is part of the current multi-touch sequence and associated with `event`.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/ignore(_:for:)-5f685)*