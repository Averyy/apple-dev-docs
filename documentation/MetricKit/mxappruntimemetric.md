# MXAppRunTimeMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the amount of time the app is active.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXAppRunTimeMetric
```

## Topics

### Reading application run time
- [var cumulativeForegroundTime: Measurement<UnitDuration>](mxappruntimemetric/cumulativeforegroundtime.md)
  The total time the app is in the foreground.
- [var cumulativeBackgroundTime: Measurement<UnitDuration>](mxappruntimemetric/cumulativebackgroundtime.md)
  The total time the app is active in the background.
- [var cumulativeBackgroundAudioTime: Measurement<UnitDuration>](mxappruntimemetric/cumulativebackgroundaudiotime.md)
  The total time the app is in the background and playing audio.
- [var cumulativeBackgroundLocationTime: Measurement<UnitDuration>](mxappruntimemetric/cumulativebackgroundlocationtime.md)
  The total time the app is in the background and using location services.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
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

- [class MXAppExitMetric](mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXForegroundExitData](mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
- [class MXBackgroundExitData](mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.
- [class MXMemoryMetric](mxmemorymetric.md)
  An object representing metrics about the app’s memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappruntimemetric)*