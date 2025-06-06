# beginRefreshing()

**Framework**: UIKit  
**Kind**: method

Tells the control that a refresh operation was started programmatically.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func beginRefreshing()
```

#### Discussion

Call this method when an external event source triggers a programmatic refresh of your scrolling view. In a table view, for example, if you use an instance of [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) to refresh the contents of the table view periodically, you would call this method as part of your timer handler. This method updates the state of the refresh control to reflect the in-progress refresh operation. When the refresh operation ends, be sure to call the [`endRefreshing()`](uirefreshcontrol/endrefreshing().md) method to return the control to its default state.

## See Also

- [func endRefreshing()](uirefreshcontrol/endrefreshing.md)
  Tells the control that a refresh operation has ended.
- [var isRefreshing: Bool](uirefreshcontrol/isrefreshing.md)
  A Boolean value indicating whether a refresh operation has been triggered and is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirefreshcontrol/beginrefreshing())*