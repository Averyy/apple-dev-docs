# MXMemoryMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the app’s memory use.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`PeakMemoryMetric`](./peakmemorymetric.md) or [`SuspendedMemoryMetric`](./suspendedmemorymetric.md) cases instead.

## Declaration

```swift
class MXMemoryMetric
```

```objc
@interface MXMemoryMetric : MXMetric
```

## Topics

### Measuring memory use
- [var averageSuspendedMemory: MXAverage<UnitInformationStorage>](./mxmemorymetric/averagesuspendedmemory.md)
  The average amount of memory in use by the app when it’s suspended.
- [var peakMemoryUsage: Measurement<UnitInformationStorage>](./mxmemorymetric/peakmemoryusage.md)
  The largest amount of memory used by the app.

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
- [class MXAppExitMetric](./mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXForegroundExitData](./mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
- [class MXBackgroundExitData](./mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmemorymetric)*