# cumulativeSuspendedWithLockedFileExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system terminated the app from the background while being suspended and having file locks.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`fileLockTerminationCount`](../backgroundterminationmetric/filelockterminationcount.md) instead.

## Declaration

```swift
var cumulativeSuspendedWithLockedFileExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeSuspendedWithLockedFileExitCount;
```

#### Discussion

A common cause for this kind of exit is writing to an SQLite database as the system is suspending the app. For information on what to do with open files and databases when transitioning to the background, see [Preparing your UI to run in the background](../../UIKit/preparing-your-ui-to-run-in-the-background.md).

## See Also

### Reading the System Termination Count
- [var cumulativeAppWatchdogExitCount: Int](./cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the background.
- [var cumulativeCPUResourceLimitExitCount: Int](./cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](./cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeMemoryPressureExitCount: Int](./cumulativememorypressureexitcount.md)
  The number of times the system terminated the app from the background to free up memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativesuspendedwithlockedfileexitcount)*