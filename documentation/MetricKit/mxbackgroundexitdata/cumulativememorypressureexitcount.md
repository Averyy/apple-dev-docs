# cumulativeMemoryPressureExitCount

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The number of times the system terminated the app from the background to free up memory.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`systemPressureTerminationCount`](../backgroundterminationmetric/systempressureterminationcount.md) instead.

## Declaration

```swift
var cumulativeMemoryPressureExitCount: Int { get }
```

```objc
@property (readonly) NSUInteger cumulativeMemoryPressureExitCount;
```

## See Also

### Reading the System Termination Count
- [var cumulativeAppWatchdogExitCount: Int](./cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the background.
- [var cumulativeCPUResourceLimitExitCount: Int](./cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](./cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeSuspendedWithLockedFileExitCount: Int](./cumulativesuspendedwithlockedfileexitcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata/cumulativememorypressureexitcount)*