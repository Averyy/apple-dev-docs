# MXForegroundExitData

**Framework**: MetricKit  
**Kind**: class

An object representing counts for the different types of foreground app exits.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MXForegroundExitData
```

## Topics

### Reading the Normal Exit Count
- [var cumulativeNormalAppExitCount: Int](mxforegroundexitdata/cumulativenormalappexitcount.md)
  The number of times the app exited normally from the foreground.
### Reading the Abnormal Exit Count
- [var cumulativeAbnormalExitCount: Int](mxforegroundexitdata/cumulativeabnormalexitcount.md)
  The number of times the app exited abnormally from the foreground.
### Reading the System Termination Count
- [var cumulativeAppWatchdogExitCount: Int](mxforegroundexitdata/cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the foreground.
- [var cumulativeMemoryResourceLimitExitCount: Int](mxforegroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.
### Reading the Crash Count
- [var cumulativeBadAccessExitCount: Int](mxforegroundexitdata/cumulativebadaccessexitcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.
- [var cumulativeIllegalInstructionExitCount: Int](mxforegroundexitdata/cumulativeillegalinstructionexitcount.md)
  The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.

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

- [var foregroundExitData: MXForegroundExitData](mxappexitmetric/foregroundexitdata.md)
  The metrics for the foreground app exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata)*