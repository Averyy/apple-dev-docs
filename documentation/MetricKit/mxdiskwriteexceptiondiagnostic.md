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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MXDiskIOMetric](mxdiskiometric.md)
  An object representing metrics about disk usage.
- [class MXDiskSpaceUsageMetric](mxdiskspaceusagemetric.md)
  An object representing metrics about your app’s disk space usage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskwriteexceptiondiagnostic)*