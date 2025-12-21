# isTracking

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the control is currently tracking touch events.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isTracking: Bool { get }
```

#### Discussion

While tracking of a touch event is in progress, the control sets the value of this property to [`true`](https://developer.apple.com/documentation/Swift/true). When tracking ends or is canceled for any reason, it sets this property to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func beginTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/begintracking(_:with:).md)
  Notifies the control when a touch event enters the control’s bounds.
- [func continueTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/continuetracking(_:with:).md)
  Notifies the control when a touch event for the control updates.
- [func endTracking(UITouch?, with: UIEvent?)](uicontrol/endtracking(_:with:).md)
  Notifies the control when a touch event associated with the control ends.
- [func cancelTracking(with: UIEvent?)](uicontrol/canceltracking(with:).md)
  Notifies the control to cancel tracking related to the specified event.
- [var isTouchInside: Bool](uicontrol/istouchinside.md)
  A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/istracking)*