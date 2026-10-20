# MXHangDiagnostic

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing a diagnostic report for an app that is too busy to handle user input responsively.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`HangDiagnostic`](./hangdiagnostic.md) instead.

## Declaration

```swift
class MXHangDiagnostic
```

```objc
@interface MXHangDiagnostic : MXDiagnostic
```

## Topics

### Reading total app hang time
- [var hangDuration: Measurement<UnitDuration>](./mxhangdiagnostic/hangduration.md)
  The amount of time the app is busy and unable to respond to user interaction.
### Viewing the call stack
- [var callStackTree: MXCallStackTree](./mxhangdiagnostic/callstacktree.md)
  The call stack for the app hang report.

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
- [class MXCPUExceptionDiagnostic](./mxcpuexceptiondiagnostic.md)
  An object representing a diagnostic report for a fatal or nonfatal CPU exception.
- [class MXCrashDiagnostic](./mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
- [class MXDiskWriteExceptionDiagnostic](./mxdiskwriteexceptiondiagnostic.md)
  An object representing a diagnostic report for a disk write exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhangdiagnostic)*