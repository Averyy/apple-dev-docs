# cumulativeCPUResourceLimitExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the background for using too much CPU time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeCPUResourceLimitExitCount: Int { get }
```

## See Also

- [var cumulativeAppWatchdogExitCount: Int](mxbackgroundexitdata/cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the background.
- [var cumulativeMemoryResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeMemoryPressureExitCount: Int](mxbackgroundexitdata/cumulativememorypressureexitcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [var cumulativeSuspendedWithLockedFileExitCount: Int](mxbackgroundexitdata/cumulativesuspendedwithlockedfileexitcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativecpuresourcelimitexitcount)*