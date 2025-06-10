# MXBackgroundExitData

**Framework**: MetricKit  
**Kind**: class

An object representing counts for the different types of background app exits.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MXBackgroundExitData
```

## Topics

### Reading the Normal Exit Count
- [var cumulativeNormalAppExitCount: Int](mxbackgroundexitdata/cumulativenormalappexitcount.md)
  The number of times the app exited normally from the background.
### Reading the Abnormal Exit Count
- [var cumulativeAbnormalExitCount: Int](mxbackgroundexitdata/cumulativeabnormalexitcount.md)
  The number of times the app exited abnormally from the background.
### Reading the System Termination Count
- [var cumulativeAppWatchdogExitCount: Int](mxbackgroundexitdata/cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the background.
- [var cumulativeCPUResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](mxbackgroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeMemoryPressureExitCount: Int](mxbackgroundexitdata/cumulativememorypressureexitcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [var cumulativeSuspendedWithLockedFileExitCount: Int](mxbackgroundexitdata/cumulativesuspendedwithlockedfileexitcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.
### Reading the Crash Count
- [var cumulativeBadAccessExitCount: Int](mxbackgroundexitdata/cumulativebadaccessexitcount.md)
  The number of times the system terminated the app from the background for attempting an invalid memory access.
- [var cumulativeIllegalInstructionExitCount: Int](mxbackgroundexitdata/cumulativeillegalinstructionexitcount.md)
  The number of times the system terminated the app from the background for attempting to execute an illegal or undefined instruction.
### Reading the Timeout Count
- [var cumulativeBackgroundTaskAssertionTimeoutExitCount: Int](mxbackgroundexitdata/cumulativebackgroundtaskassertiontimeoutexitcount.md)
  The number of times the system terminated the app from the background for exceeding the allocated time for a background task.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var backgroundExitData: MXBackgroundExitData](mxappexitmetric/backgroundexitdata.md)
  The metrics for the background app exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata)*