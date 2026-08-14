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
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXCPUExceptionDiagnostic](mxcpuexceptiondiagnostic.md)
  An object representing a diagnostic report for a fatal or nonfatal CPU exception.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
- [class MXHangDiagnostic](mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.
- [class MXDiskWriteExceptionDiagnostic](mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchdiagnostic)*