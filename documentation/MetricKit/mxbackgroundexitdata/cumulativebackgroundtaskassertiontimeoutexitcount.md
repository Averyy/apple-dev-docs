# cumulativeBackgroundTaskAssertionTimeoutExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system terminated the app from the background for exceeding the allocated time for a background task.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`taskTimeoutTerminationCount`](../backgroundterminationmetric/tasktimeoutterminationcount.md) instead.

## Declaration

```swift
var cumulativeBackgroundTaskAssertionTimeoutExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeBackgroundTaskAssertionTimeoutExitCount;
```

## Discussion

This exit usually occurs when the app fails to call [`endBackgroundTask(_:)`](../../UIKit/uiapplication/endbackgroundtask%28_%29.md) as soon as a background task is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativebackgroundtaskassertiontimeoutexitcount)*