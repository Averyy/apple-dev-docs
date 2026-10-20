# continueTracking(_:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the control when a touch event for the control updates.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func continueTracking(_ touch: UITouch, with event: UIEvent?) -> Bool
```

```objc
- (BOOL) continueTrackingWithTouch:(UITouch *) touch withEvent:(UIEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) if the control should continue tracking touch events or [`false`](../../Swift/false.md) if it should stop. This value is used to update the [`isTracking`](./istracking.md) property of the control.

#### Discussion

This method is called repeatedly while a touch event is being tracked inside the control’s bounds. The default implementation of this method always returns [`true`](../../Swift/true.md). Subclasses can override this method and use it to update their state based on changes to the touch event. If you want to continue tracking the touch event, return [`true`](../../Swift/true.md). If you want to stop tracking the touch event, return [`false`](../../Swift/false.md).

## Parameters

- `touch`: The touch object containing updated information.
- `event`: The event object containing the touch event.

## See Also

### Tracking touches and redrawing controls
- [func beginTracking(UITouch, with: UIEvent?) -> Bool](./begintracking%28_,with%29.md)
  Notifies the control when a touch event enters the control’s bounds.
- [func endTracking(UITouch?, with: UIEvent?)](./endtracking%28_,with%29.md)
  Notifies the control when a touch event associated with the control ends.
- [func cancelTracking(with: UIEvent?)](./canceltracking%28with%29.md)
  Notifies the control to cancel tracking related to the specified event.
- [var isTracking: Bool](./istracking.md)
  A Boolean value that indicates whether the control is currently tracking touch events.
- [var isTouchInside: Bool](./istouchinside.md)
  A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/continuetracking(_:with:))*