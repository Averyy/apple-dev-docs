# MXCPUExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: class

An object representing a diagnostic report for a fatal or nonfatal CPU exception.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXCPUExceptionDiagnostic
```

#### Overview

A CPU exception occurs when your app uses an excessive amount of CPU time over a short period.

## Topics

### Viewing the call stack
- [var callStackTree: MXCallStackTree](mxcpuexceptiondiagnostic/callstacktree.md)
  The app call stack associated with the CPU exception.
### Viewing app CPU time
- [var totalCPUTime: Measurement<UnitDuration>](mxcpuexceptiondiagnostic/totalcputime.md)
  The total CPU time used during the exception.
- [var totalSampledTime: Measurement<UnitDuration>](mxcpuexceptiondiagnostic/totalsampledtime.md)
  The total time the app was sampled during the exception.

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

- [class MXAppLaunchDiagnostic](mxapplaunchdiagnostic.md)
  A diagnostic subclass that encapsulates app launch diagnostic reports.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
- [class MXHangDiagnostic](mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.
- [class MXDiskWriteExceptionDiagnostic](mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpuexceptiondiagnostic)*