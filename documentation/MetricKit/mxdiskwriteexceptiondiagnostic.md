# MXDiskWriteExceptionDiagnostic

**Framework**: MetricKit  
**Kind**: class

An object representing a diagnostic report for a disk write exception.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXDiskWriteExceptionDiagnostic
```

#### Overview

A disk write exception occurs when the app writes an excessive amount of data to the disk.

## Topics

### Reading total disk writes
- [var totalWritesCaused: Measurement<UnitInformationStorage>](mxdiskwriteexceptiondiagnostic/totalwritescaused.md)
  The total amount of data written to disk or other long-term storage during the disk write exception.
### Viewing the call stack
- [var callStackTree: MXCallStackTree](mxdiskwriteexceptiondiagnostic/callstacktree.md)
  The call stack for the disk write exception.

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

- [class MXAppLaunchDiagnostic](mxapplaunchdiagnostic.md)
  A diagnostic subclass that encapsulates app launch diagnostic reports.
- [class MXCPUExceptionDiagnostic](mxcpuexceptiondiagnostic.md)
  An object representing a diagnostic report for a fatal or nonfatal CPU exception.
- [class MXCrashDiagnostic](mxcrashdiagnostic.md)
  An object representing a diagnostic report for an app crash.
- [class MXHangDiagnostic](mxhangdiagnostic.md)
  An object representing a diagnostic report for an app that is too busy to handle user input responsively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskwriteexceptiondiagnostic)*