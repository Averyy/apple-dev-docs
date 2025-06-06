# cumulativeMemoryPressureExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the background to free up memory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeMemoryPressureExitCount: Int { get }
```

## See Also

- [var cumulativeAppWatchdogExitCount: Int](mxbackgroundexitdata/cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the background.
- [var cumulativeCPUResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeSuspendedWithLockedFileExitCount: Int](mxbackgroundexitdata/cumulativesuspendedwithlockedfileexitcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativememorypressureexitcount)*