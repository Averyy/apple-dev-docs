# cumulativeSuspendedWithLockedFileExitCount

**Framework**: MetricKit  
**Kind**: property

The number of times the system terminated the app from the background while being suspended and having file locks.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var cumulativeSuspendedWithLockedFileExitCount: Int { get }
```

#### Discussion

A common cause for this kind of exit is writing to an SQLite database as the system is suspending the app. For information on what to do with open files and databases when transitioning to the background, see [`Preparing your UI to run in the background`](https://developer.apple.com/documentation/UIKit/preparing-your-ui-to-run-in-the-background).

## See Also

- [var cumulativeAppWatchdogExitCount: Int](mxbackgroundexitdata/cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the background.
- [var cumulativeCPUResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeMemoryPressureExitCount: Int](mxbackgroundexitdata/cumulativememorypressureexitcount.md)
  The number of times the system terminated the app from the background to free up memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativesuspendedwithlockedfileexitcount)*