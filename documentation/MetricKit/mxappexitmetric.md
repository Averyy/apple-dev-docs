# MXAppExitMetric

**Framework**: MetricKit  
**Kind**: class

An object representing metrics about the types of foreground and background app exits.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class MXAppExitMetric
```

## Topics

### Reading the foreground exit data
- [var foregroundExitData: MXForegroundExitData](mxappexitmetric/foregroundexitdata.md)
  The metrics for the foreground app exits.
- [class MXForegroundExitData](mxforegroundexitdata.md)
  An object representing counts for the different types of foreground app exits.
### Reading the background exit data
- [var backgroundExitData: MXBackgroundExitData](mxappexitmetric/backgroundexitdata.md)
  The metrics for the background app exits.
- [class MXBackgroundExitData](mxbackgroundexitdata.md)
  An object representing counts for the different types of background app exits.

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
- [class MXAppRunTimeMetric](mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXMemoryMetric](mxmemorymetric.md)
  An object representing metrics about the app’s memory use.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxappexitmetric)*