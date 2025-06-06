# isTouchInside

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether a tracked touch event is currently inside the control’s bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isTouchInside: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the location of the most recent touch event is inside the control’s bounds or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

#### Discussion

While tracking of a touch event is ongoing, the control updates the value of this property to indicate whether the most recent touch is still inside the control’s bounds. The control uses this information to trigger specific events. For example, touch events entering or exiting a control trigger appropriate drag events.

## See Also

- [func beginTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/begintracking(_:with:).md)
  Notifies the control when a touch event enters the control’s bounds.
- [func continueTracking(UITouch, with: UIEvent?) -> Bool](uicontrol/continuetracking(_:with:).md)
  Notifies the control when a touch event for the control updates.
- [func endTracking(UITouch?, with: UIEvent?)](uicontrol/endtracking(_:with:).md)
  Notifies the control when a touch event associated with the control ends.
- [func cancelTracking(with: UIEvent?)](uicontrol/canceltracking(with:).md)
  Notifies the control to cancel tracking related to the specified event.
- [var isTracking: Bool](uicontrol/istracking.md)
  A Boolean value that indicates whether the control is currently tracking touch events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/istouchinside)*