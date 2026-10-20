# touchesEstimatedPropertiesUpdated(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func touchesEstimatedPropertiesUpdated(_ touches: Set<UITouch>)
```

```objc
- (void) touchesEstimatedPropertiesUpdated:(NSSet<UITouch *> *) touches;
```

#### Discussion

The default implementation of this method does nothing. Subclasses may override it and use it to process updates to touches.

UIKit calls this method to report updates to properties that were previously declared to be estimates through [`touchesBegan(_:with:)`](./touchesbegan%28_,with%29.md),  [`touchesMoved(_:with:)`](./touchesmoved%28_,with%29.md) or [`touchesEnded(_:with:)`](../uiresponder/touchesended%28_,with%29.md), and where declared to expect updates by having at least one property set in [`estimatedPropertiesExpectingUpdates`](../uitouch/estimatedpropertiesexpectingupdates.md).

Use the [`estimationUpdateIndex`](../uitouch/estimationupdateindex.md) property to correlate the previous state of the touch with the updated state incoming in this method. The updated values are denoted by having a cleared state in the [`estimatedPropertiesExpectingUpdates`](../uitouch/estimatedpropertiesexpectingupdates.md) bit mask. Although most properties end up with a cleared [`estimatedProperties`](../uitouch/estimatedproperties.md) flag, a property can stay in the estimated state because of hardware considerations. This behavior allows the client to decide to replace the estimate with a more domain-specific estimate, based on the other touches it receives.

## Parameters

- `touches`: The array of [`UITouch`](../uitouch.md) objects containing updated properties.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/touchesestimatedpropertiesupdated(_:))*