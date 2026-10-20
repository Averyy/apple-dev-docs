# MXCPUExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing a diagnostic report for a fatal or nonfatal CPU exception.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CPUExceptionDiagnostic`](./cpuexceptiondiagnostic.md) instead.

## Declaration

```swift
class MXCPUExceptionDiagnostic
```

```objc
@interface MXCPUExceptionDiagnostic : MXDiagnostic
```

#### Overview

A CPU exception occurs when your app uses an excessive amount of CPU time over a short period.

## Topics

### Viewing the call stack
- [var callStackTree: MXCallStackTree](./mxcpuexceptiondiagnostic/callstacktree.md)
  The app call stack associated with the CPU exception.
### Viewing app CPU time
- [var totalCPUTime: Measurement<UnitDuration>](./mxcpuexceptiondiagnostic/totalcputime.md)
  The total CPU time used during the exception.
- [var totalSampledTime: Measurement<UnitDuration>](./mxcpuexceptiondiagnostic/totalsampledtime.md)
  The total time the app was sampled during the exception.

## Relationships

### Inherits From
- [MXDiagnostic](./mxdiagnostic.md)
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

### Performance diagnostics
- [class MXAppLaunchDiagnostic](./mxapplaunchdiagnostic.md)
  A diagnostic subclass that encapsulates app launch diagnostic reports.
- [class MXCrashDiagnostic](./mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
- [class MXHangDiagnostic](./mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.
- [class MXDiskWriteExceptionDiagnostic](./mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcpuexceptiondiagnostic)*