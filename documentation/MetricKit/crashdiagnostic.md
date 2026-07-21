# CrashDiagnostic

**Framework**: MetricKit  
**Kind**: struct

A diagnostic report that describes a crash that occurred.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CrashDiagnostic
```

## Mentions

- [Monitoring app performance with MetricKit](monitoring-app-performance-with-metrickit.md)

#### Discussion

This carries a [`CallStackTree`](callstacktree.md) along with crash-specific metadata including the exception type, exception code, signal, and optional Objective-C exception reason.

Use [`terminationCategory`](crashdiagnostic/terminationcategory-swift.property.md) to correlate this crash with the aggregate termination counts in [`ForegroundTerminationMetric`](foregroundterminationmetric.md) and [`BackgroundTerminationMetric`](backgroundterminationmetric.md):

```swift
if let category = diagnostic.terminationCategory {
    switch category {
    case .watchdog:
        flagWatchdogTermination()
    case .badAccess:
        flagBadAccessCrash()
    default:
        break
    }
}
```

## Topics

### Call stack
- [let callStackTree: CallStackTree](crashdiagnostic/callstacktree.md)
  The application call stack tree associated with this crash.
### Exception details
- [let exceptionType: Int?](crashdiagnostic/exceptiontype.md)
  The name of the Mach exception that terminated the app.
- [let exceptionCode: UInt64?](crashdiagnostic/exceptioncode.md)
  Processor specific information about the exception.
- [let signal: Int?](crashdiagnostic/signal.md)
  The signal associated with this crash.
- [let exceptionReason: CrashDiagnostic.ObjectiveCExceptionReason?](crashdiagnostic/exceptionreason.md)
  The exception reason for an uncaught ObjC exception.
- [let virtualMemoryRegionInfo: String?](crashdiagnostic/virtualmemoryregioninfo.md)
  Details about memory that the app incorrectly accessed.
### Termination counts
- [let terminationCategory: CrashDiagnostic.TerminationCategory?](crashdiagnostic/terminationcategory-swift.property.md)
  The category of termination that caused this crash.
- [let terminationReason: CrashDiagnostic.TerminationReason?](crashdiagnostic/terminationreason-swift.property.md)
  The reason the app was terminated as a human-readable string.
### Structures
- [CrashDiagnostic.ObjectiveCExceptionReason](crashdiagnostic/objectivecexceptionreason.md)
  Detailed information about an uncaught Objective-C exception that caused a crash.
- [CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct.md)
  A value that describes the category of termination that caused a crash.
- [CrashDiagnostic.TerminationReason](crashdiagnostic/terminationreason-swift.struct.md)
  The reason the app was terminated, as a human-readable string.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HangDiagnostic](hangdiagnostic.md)
  A diagnostic for an app that was too busy to handle user input responsively.
- [struct AppLaunchDiagnostic](applaunchdiagnostic.md)
  A diagnostic report for an app launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic)*