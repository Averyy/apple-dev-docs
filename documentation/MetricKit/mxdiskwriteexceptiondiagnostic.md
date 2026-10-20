# MXDiskWriteExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object representing a diagnostic report for a disk write exception.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiskWriteExceptionDiagnostic`](./diskwriteexceptiondiagnostic.md) instead.

## Declaration

```swift
class MXDiskWriteExceptionDiagnostic
```

```objc
@interface MXDiskWriteExceptionDiagnostic : MXDiagnostic
```

#### Overview

A disk write exception occurs when the app writes an excessive amount of data to the disk.

## Topics

### Reading total disk writes
- [var totalWritesCaused: Measurement<UnitInformationStorage>](./mxdiskwriteexceptiondiagnostic/totalwritescaused.md)
  The total amount of data written to disk or other long-term storage during the disk write exception.
### Viewing the call stack
- [var callStackTree: MXCallStackTree](./mxdiskwriteexceptiondiagnostic/callstacktree.md)
  The call stack for the disk write exception.

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
- [class MXHangDiagnostic](./mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskwriteexceptiondiagnostic)*