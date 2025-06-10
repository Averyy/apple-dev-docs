# cumulativeAppWatchdogExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system watchdog terminated the app from the background.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeAppWatchdogExitCount: Int { get }
```

#### Discussion

The most common reasons the system watchdog terminates an app are taking too long to:

- Launch
- Terminate
- Respond to system events

## See Also

- [var cumulativeCPUResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeMemoryPressureExitCount: Int](mxbackgroundexitdata/cumulativememorypressureexitcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [var cumulativeSuspendedWithLockedFileExitCount: Int](mxbackgroundexitdata/cumulativesuspendedwithlockedfileexitcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativeappwatchdogexitcount)*