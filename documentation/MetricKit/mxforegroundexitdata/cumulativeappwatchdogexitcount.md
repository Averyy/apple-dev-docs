# cumulativeAppWatchdogExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system watchdog terminated the app from the foreground.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`watchdogTerminationCount`](../foregroundterminationmetric/watchdogterminationcount.md) instead.

## Declaration

```swift
var cumulativeAppWatchdogExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeAppWatchdogExitCount;
```

## Discussion

The most common reasons the system watchdog terminates an app are taking too long to:

- Launch
- Respond to system events

## See Also

### Reading the System Termination Count
- [var cumulativeMemoryResourceLimitExitCount: Int](./cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata/cumulativeappwatchdogexitcount)*