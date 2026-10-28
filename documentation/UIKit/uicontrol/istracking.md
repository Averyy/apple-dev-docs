# isTracking

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the control is currently tracking touch events.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isTracking: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isTracking) BOOL tracking;
```

## Discussion

While tracking of a touch event is in progress, the control sets the value of this property to [`true`](../../Swift/true.md). When tracking ends or is canceled for any reason, it sets this property to [`false`](../../Swift/false.md).

## See Also

### Tracking touches and redrawing controls
- [func beginTracking(UITouch, with: UIEvent?) -> Bool](./begintracking%28_,with%29.md)
  Notifies the control when a touch event enters the control’s bounds.
- [func continueTracking(UITouch, with: UIEvent?) -> Bool](./continuetracking%28_,with%29.md)
  Notifies the control when a touch event for the control updates.
- [func endTracking(UITouch?, with: UIEvent?)](./endtracking%28_,with%29.md)
  Notifies the control when a touch event associated with the control ends.
- [func cancelTracking(with: UIEvent?)](./canceltracking%28with%29.md)
  Notifies the control to cancel tracking related to the specified event.
- [var isTouchInside: Bool](./istouchinside.md)
  A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/istracking)*