# MXBackgroundExitData

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing counts for the different types of background app exits.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`BackgroundTerminationMetric`](./backgroundterminationmetric.md) instead.

## Declaration

```swift
class MXBackgroundExitData
```

```objc
@interface MXBackgroundExitData : NSObject
```

## Topics

### Reading the Normal Exit Count
- [var cumulativeNormalAppExitCount: Int](./mxbackgroundexitdata/cumulativenormalappexitcount.md)
  The number of times the app exited normally from the background.
### Reading the Abnormal Exit Count
- [var cumulativeAbnormalExitCount: Int](./mxbackgroundexitdata/cumulativeabnormalexitcount.md)
  The number of times the app exited abnormally from the background.
### Reading the System Termination Count
- [var cumulativeAppWatchdogExitCount: Int](./mxbackgroundexitdata/cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the background.
- [var cumulativeCPUResourceLimitExitCount: Int](./mxbackgroundexitdata/cumulativecpuresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [var cumulativeMemoryResourceLimitExitCount: Int](./mxbackgroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [var cumulativeMemoryPressureExitCount: Int](./mxbackgroundexitdata/cumulativememorypressureexitcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [var cumulativeSuspendedWithLockedFileExitCount: Int](./mxbackgroundexitdata/cumulativesuspendedwithlockedfileexitcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.
### Reading the Crash Count
- [var cumulativeBadAccessExitCount: Int](./mxbackgroundexitdata/cumulativebadaccessexitcount.md)
  The number of times the system terminated the app from the background for attempting an invalid memory access.
- [var cumulativeIllegalInstructionExitCount: Int](./mxbackgroundexitdata/cumulativeillegalinstructionexitcount.md)
  The number of times the system terminated the app from the background for attempting to execute an illegal or undefined instruction.
### Reading the Timeout Count
- [var cumulativeBackgroundTaskAssertionTimeoutExitCount: Int](./mxbackgroundexitdata/cumulativebackgroundtaskassertiontimeoutexitcount.md)
  The number of times the system terminated the app from the background for exceeding the allocated time for a background task.
### Initializers
- [init?(coder: NSCoder)](./mxbackgroundexitdata/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### App performance metrics
- [class MXAppRunTimeMetric](./mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXAppExitMetric](./mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXForegroundExitData](./mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
- [class MXMemoryMetric](./mxmemorymetric.md)
  An object representing metrics about the app’s memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxbackgroundexitdata)*