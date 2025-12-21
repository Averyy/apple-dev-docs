# beginTracking(_:with:)

**Framework**: UIKit  
**Kind**: method

Notifies the control when a touch event enters the control’s bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func beginTracking(_ touch: UITouch, with event: UIEvent?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the control should continue tracking touch events or [`false`](https://developer.apple.com/documentation/Swift/false) if it should stop. This value is used to update the [`isTracking`](uicontrol/istracking.md) property of the control.

#### Discussion

The default implementation of this method always returns [`true`](https://developer.apple.com/documentation/Swift/true). Subclasses can override this method and use it to respond to events. Use the provided event information to detect which part of your control was hit and to set up any initial state information. If you want to continue tracking the touch event, return [`true`](https://developer.apple.com/documentation/Swift/true). If you want to stop tracking the touch event, return [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `touch`: The object containing information about the touch event.
- `event`: The event object containing the touch event.

## See Also

- [func continueTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/continuetracking(_:with:).md)
  Notifies the control when a touch event for the control updates.
- [func endTracking(UITouch?, with: UIEvent?)](uicontrol/endtracking(_:with:).md)
  Notifies the control when a touch event associated with the control ends.
- [func cancelTracking(with: UIEvent?)](uicontrol/canceltracking(with:).md)
  Notifies the control to cancel tracking related to the specified event.
- [var isTracking: Bool](uicontrol/istracking.md)
  A Boolean value that indicates whether the control is currently tracking touch events.
- [var isTouchInside: Bool](uicontrol/istouchinside.md)
  A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/begintracking(_:with:))*