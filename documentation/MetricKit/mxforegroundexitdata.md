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
### Initializers
- [init?(coder: NSCoder)](mxforegroundexitdata/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXAppRunTimeMetric](mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXAppExitMetric](mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXBackgroundExitData](mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.
- [class MXMemoryMetric](mxmemorymetric.md)
  An object representing metrics about the app’s memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata)*