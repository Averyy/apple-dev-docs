# MXAppLaunchDiagnostic

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

A diagnostic subclass that encapsulates app launch diagnostic reports.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`AppLaunchDiagnostic`](./applaunchdiagnostic.md) instead.

## Declaration

```swift
class MXAppLaunchDiagnostic
```

```objc
@interface MXAppLaunchDiagnostic : MXDiagnostic
```

## Topics

### Reading app launch metrics
- [var callStackTree: MXCallStackTree](./mxapplaunchdiagnostic/callstacktree.md)
  The call stack tree associated with the app launch.
- [var launchDuration: Measurement<UnitDuration>](./mxapplaunchdiagnostic/launchduration.md)
  The total app launch duration.

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
- [class MXCPUExceptionDiagnostic](./mxcpuexceptiondiagnostic.md)
  An object representing a diagnostic report for a fatal or nonfatal CPU exception.
- [class MXCrashDiagnostic](./mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
- [class MXHangDiagnostic](./mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.
- [class MXDiskWriteExceptionDiagnostic](./mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxapplaunchdiagnostic)*