# endRefreshing()

**Framework**: UIKit  
**Kind**: method

Tells the control that a refresh operation has ended.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func endRefreshing()
```

#### Discussion

Call this method at the end of any refresh operation (whether it was initiated programmatically or by the user) to return the refresh control to its default state. If the refresh control is at least partially visible, calling this method also hides it. If animations are also enabled, the control is hidden using an animation.

## See Also

- [func beginRefreshing()](uirefreshcontrol/beginrefreshing.md)
  Tells the control that a refresh operation was started programmatically.
- [var isRefreshing: Bool](uirefreshcontrol/isrefreshing.md)
  A Boolean value indicating whether a refresh operation has been triggered and is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirefreshcontrol/endrefreshing())*