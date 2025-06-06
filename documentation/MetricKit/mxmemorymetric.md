# MXMemoryMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the app’s memory use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MXMemoryMetric
```

## Topics

### Measuring memory use
- [var averageSuspendedMemory: MXAverage<UnitInformationStorage>](mxmemorymetric/averagesuspendedmemory.md)
  The average amount of memory in use by the app when it’s suspended.
- [var peakMemoryUsage: Measurement<UnitInformationStorage>](mxmemorymetric/peakmemoryusage.md)
  The largest amount of memory used by the app.

## Relationships

### Inherits From
- [MXMetric](mxmetric.md)
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

- [class MXAppLaunchDiagnostic](mxapplaunchdiagnostic.md)
  A diagnostic subclass that encapsulates app launch diagnostic reports.
- [class MXAppExitMetric](mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXAppRunTimeMetric](mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmemorymetric)*