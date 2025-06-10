# cumulativeBackgroundTaskAssertionTimeoutExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the background for exceeding the allocated time for a background task.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeBackgroundTaskAssertionTimeoutExitCount: Int { get }
```

#### Discussion

This exit usually occurs when the app fails to call [`endBackgroundTask(_:)`](https://developer.apple.com/documentation/UIKit/UIApplication/endBackgroundTask(_:)) as soon as a background task is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativebackgroundtaskassertiontimeoutexitcount)*