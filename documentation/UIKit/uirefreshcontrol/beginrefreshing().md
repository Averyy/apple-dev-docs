# beginRefreshing()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the control that a refresh operation was started programmatically.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func beginRefreshing()
```

```objc
- (void) beginRefreshing;
```

## Discussion

Call this method when an external event source triggers a programmatic refresh of your scrolling view. In a table view, for example, if you use an instance of [`Timer`](../../Foundation/timer.md) to refresh the contents of the table view periodically, you would call this method as part of your timer handler. This method updates the state of the refresh control to reflect the in-progress refresh operation. When the refresh operation ends, be sure to call the [`endRefreshing()`](./endrefreshing%28%29.md) method to return the control to its default state.

## See Also

### Managing the refresh status
- [func endRefreshing()](./endrefreshing%28%29.md)
  Tells the control that a refresh operation has ended.
- [var isRefreshing: Bool](./isrefreshing.md)
  A Boolean value indicating whether a refresh operation has been triggered and is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirefreshcontrol/beginrefreshing())*