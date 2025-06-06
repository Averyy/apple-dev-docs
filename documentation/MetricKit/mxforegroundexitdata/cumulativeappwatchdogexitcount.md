# cumulativeAppWatchdogExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system watchdog terminated the app from the foreground.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeAppWatchdogExitCount: Int { get }
```

#### Discussion

The most common reasons the system watchdog terminates an app are taking too long to:

- Launch
- Respond to system events

## See Also

- [var cumulativeMemoryResourceLimitExitCount: Int](mxforegroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata/cumulativeappwatchdogexitcount)*