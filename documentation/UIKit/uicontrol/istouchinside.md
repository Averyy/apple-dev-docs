# isTouchInside

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isTouchInside: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isTouchInside) BOOL touchInside;
```

#### Return Value

[`true`](../../Swift/true.md) if the location of the most recent touch event is inside the control’s bounds or [`false`](../../Swift/false.md) if it is not.

#### Discussion

While tracking of a touch event is ongoing, the control updates the value of this property to indicate whether the most recent touch is still inside the control’s bounds. The control uses this information to trigger specific events. For example, touch events entering or exiting a control trigger appropriate drag events.

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
- [var isTracking: Bool](./istracking.md)
  A Boolean value that indicates whether the control is currently tracking touch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/istouchinside)*