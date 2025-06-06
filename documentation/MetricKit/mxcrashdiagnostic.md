# MXCrashDiagnostic

**Framework**: MetricKit  
**Kind**: class

An object representing a diagnostic report for an app crash.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXCrashDiagnostic
```

## Topics

### Viewing exception details
- [var exceptionType: NSNumber?](mxcrashdiagnostic/exceptiontype.md)
  The Mach exception type of the crash.
- [var exceptionCode: NSNumber?](mxcrashdiagnostic/exceptioncode.md)
  The encoded processor-specific information for the crash.
- [var signal: NSNumber?](mxcrashdiagnostic/signal.md)
  The signal associated with the crash.
- [var exceptionReason: MXCrashDiagnosticObjectiveCExceptionReason?](mxcrashdiagnostic/exceptionreason.md)
- [var terminationReason: String?](mxcrashdiagnostic/terminationreason.md)
  The reason the app was terminated as a human-readable string.
- [var virtualMemoryRegionInfo: String?](mxcrashdiagnostic/virtualmemoryregioninfo.md)
  Information about the region of memory an app accessed incorrectly, resulting in a bad-access crash.
### Viewing the call stack
- [var callStackTree: MXCallStackTree](mxcrashdiagnostic/callstacktree.md)
  The call stack for the crash.

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
- [class MXAppExitMetric](mxappexitmetric.md)
  An object representing metrics about the types of foreground and background app exits.
- [class MXAppRunTimeMetric](mxappruntimemetric.md)
  An object representing metrics about the amount of time the app is active.
- [class MXMemoryMetric](mxmemorymetric.md)
  An object representing metrics about the app’s memory use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic)*