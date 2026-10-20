# MXForegroundExitData

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing counts for the different types of foreground app exits.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`ForegroundTerminationMetric`](./foregroundterminationmetric.md) instead.

## Declaration

```swift
class MXForegroundExitData
```

```objc
@interface MXForegroundExitData : NSObject
```

## Topics

### Reading the Normal Exit Count
- [var cumulativeNormalAppExitCount: Int](./mxforegroundexitdata/cumulativenormalappexitcount.md)
  The number of times the app exited normally from the foreground.
### Reading the Abnormal Exit Count
- [var cumulativeAbnormalExitCount: Int](./mxforegroundexitdata/cumulativeabnormalexitcount.md)
  The number of times the app exited abnormally from the foreground.
### Reading the System Termination Count
- [var cumulativeAppWatchdogExitCount: Int](./mxforegroundexitdata/cumulativeappwatchdogexitcount.md)
  The number of times the system watchdog terminated the app from the foreground.
- [var cumulativeMemoryResourceLimitExitCount: Int](./mxforegroundexitdata/cumulativememoryresourcelimitexitcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.
### Reading the Crash Count
- [var cumulativeBadAccessExitCount: Int](./mxforegroundexitdata/cumulativebadaccessexitcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.
- [var cumulativeIllegalInstructionExitCount: Int](./mxforegroundexitdata/cumulativeillegalinstructionexitcount.md)
  The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.
### Initializers
- [init?(coder: NSCoder)](./mxforegroundexitdata/init%28coder%29.md)

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
- [class MXBackgroundExitData](./mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.
- [class MXMemoryMetric](./mxmemorymetric.md)
  An object representing metrics about the app’s memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxforegroundexitdata)*