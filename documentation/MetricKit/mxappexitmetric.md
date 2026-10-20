# MXAppExitMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the types of foreground and background app exits.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`ForegroundTerminationMetric`](./foregroundterminationmetric.md) or [`BackgroundTerminationMetric`](./backgroundterminationmetric.md) cases instead.

## Declaration

```swift
class MXAppExitMetric
```

```objc
@interface MXAppExitMetric : MXMetric
```

## Topics

### Reading the foreground exit data
- [var foregroundExitData: MXForegroundExitData](./mxappexitmetric/foregroundexitdata.md)
  The metrics for the foreground app exits.
- [class MXForegroundExitData](./mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
### Reading the background exit data
- [var backgroundExitData: MXBackgroundExitData](./mxappexitmetric/backgroundexitdata.md)
  The metrics for the background app exits.
- [class MXBackgroundExitData](./mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.

## Relationships

### Inherits From
- [MXMetric](./mxmetric.md)
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
- [class MXForegroundExitData](./mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
- [class MXBackgroundExitData](./mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.
- [class MXMemoryMetric](./mxmemorymetric.md)
  An object representing metrics about the app’s memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappexitmetric)*