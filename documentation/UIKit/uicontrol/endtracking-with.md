# endTracking(_:with:)

**Framework**: UIKit  
**Kind**: method

Notifies the control when a touch event associated with the control ends.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func endTracking(_ touch: UITouch?, with event: UIEvent?)
```

#### Discussion

This method is called at the end of a sequence of touch events inside the control’s bounds. Subclasses can override this method and use it to perform any actions relevant to the completion of the touch sequence. You should also use it to perform any cleanup associated with tracking the event.

If you override this method, you must call `super` at some point in your implementation. The default implementation updates the [`isTracking`](uicontrol/istracking.md) property of the control.

## Parameters

- `touch`: The touch object containing the final touch information.
- `event`: The event object containing the touch event.

## See Also

- [func beginTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/begintracking(_:with:).md)
  Notifies the control when a touch event enters the control’s bounds.
- [func continueTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/continuetracking(_:with:).md)
  Notifies the control when a touch event for the control updates.
- [func cancelTracking(with: UIEvent?)](uicontrol/canceltracking(with:).md)
  Notifies the control to cancel tracking related to the specified event.
- [var isTracking: Bool](uicontrol/istracking.md)
  A Boolean value that indicates whether the control is currently tracking touch events.
- [var isTouchInside: Bool](uicontrol/istouchinside.md)
  A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/endtracking(_:with:))*