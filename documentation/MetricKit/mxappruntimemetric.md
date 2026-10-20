# MXAppRunTimeMetric

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing metrics about the amount of time the app is active.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](./metricresult.md), and read the [`TotalForegroundTimeMetric`](./totalforegroundtimemetric.md), [`TotalBackgroundTimeMetric`](./totalbackgroundtimemetric.md), [`TotalBackgroundAudioTimeMetric`](./totalbackgroundaudiotimemetric.md), or [`TotalBackgroundLocationTimeMetric`](./totalbackgroundlocationtimemetric.md) cases instead.

## Declaration

```swift
class MXAppRunTimeMetric
```

```objc
@interface MXAppRunTimeMetric : MXMetric
```

## Topics

### Reading application run time
- [var cumulativeForegroundTime: Measurement<UnitDuration>](./mxappruntimemetric/cumulativeforegroundtime.md)
  The total time the app is in the foreground.
- [var cumulativeBackgroundTime: Measurement<UnitDuration>](./mxappruntimemetric/cumulativebackgroundtime.md)
  The total time the app is active in the background.
- [var cumulativeBackgroundAudioTime: Measurement<UnitDuration>](./mxappruntimemetric/cumulativebackgroundaudiotime.md)
  The total time the app is in the background and playing audio.
- [var cumulativeBackgroundLocationTime: Measurement<UnitDuration>](./mxappruntimemetric/cumulativebackgroundlocationtime.md)
  The total time the app is in the background and using location services.

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
- [class MXAppExitMetric](./mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXForegroundExitData](./mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
- [class MXBackgroundExitData](./mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.
- [class MXMemoryMetric](./mxmemorymetric.md)
  An object representing metrics about the app’s memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappruntimemetric)*