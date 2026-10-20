# cumulativeMemoryResourceLimitExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system terminated the app from the foreground for using too much memory.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`memoryLimitTerminationCount`](../foregroundterminationmetric/memorylimitterminationcount.md) instead.

## Declaration

```swift
var cumulativeMemoryResourceLimitExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeMemoryResourceLimitExitCount;
```

## See Also

### Reading the System Termination Count
- [var cumulativeAppWatchdogExitCount: Int](./cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata/cumulativememoryresourcelimitexitcount)*