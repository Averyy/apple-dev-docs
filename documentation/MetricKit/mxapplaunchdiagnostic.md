# MXAppLaunchDiagnostic

**Framework**: MetricKit  
**Kind**: class

A diagnostic subclass that encapsulates app launch diagnostic reports.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class MXAppLaunchDiagnostic
```

## Topics

### Reading app launch metrics
- [var callStackTree: MXCallStackTree](mxapplaunchdiagnostic/callstacktree.md)
  The call stack tree associated with the app launch.
- [var launchDuration: Measurement<UnitDuration>](mxapplaunchdiagnostic/launchduration.md)
  The total app launch duration.

## Relationships

### Inherits From
- [MXDiagnostic](mxdiagnostic.md)
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

- [class MXAppExitMetric](mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXAppRunTimeMetric](mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXMemoryMetric](mxmemorymetric.md)
  An object representing metrics about the app’s memory use.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchdiagnostic)*