# cumulativeAppWatchdogExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system watchdog terminated the app from the background.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`watchdogTerminationCount`](../backgroundterminationmetric/watchdogterminationcount.md) instead.

## Declaration

```swift
var cumulativeAppWatchdogExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeAppWatchdogExitCount;
```

#### Discussion

The most common reasons the system watchdog terminates an app are taking too long to:

- Launch
- Terminate
- Respond to system events

## See Also

### Reading the System Termination Count
- [var cumulativeCPUResourceLimitExitCount: Int](./cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](./cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeMemoryPressureExitCount: Int](./cumulativememorypressureexitcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [var cumulativeSuspendedWithLockedFileExitCount: Int](./cumulativesuspendedwithlockedfileexitcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativeappwatchdogexitcount)*