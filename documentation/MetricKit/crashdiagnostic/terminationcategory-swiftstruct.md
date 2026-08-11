# CrashDiagnostic.TerminationCategory

**Framework**: MetricKit  
**Kind**: struct

A value that describes the category of termination that caused a crash.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TerminationCategory
```

#### Discussion

Use `TerminationCategory` to correlate individual crash diagnostics with the aggregate termination counts reported by [`ForegroundTerminationMetric`](foregroundterminationmetric.md) and [`BackgroundTerminationMetric`](backgroundterminationmetric.md). Each category corresponds to a specific count property on one or both of those metric types.

## Topics

### Termination categories
- [static let badAccess: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/badaccess.md)
  The app was terminated for attempting an invalid memory access.
- [static let abnormal: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/abnormal.md)
  The app terminated abnormally, typically due to an uncaught exception or call to `abort()`.
- [static let illegalInstruction: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/illegalinstruction.md)
  The app was terminated for executing an illegal or undefined instruction.
- [static let watchdog: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/watchdog.md)
  The app was terminated by the system watchdog for failing to respond in time.
- [static let taskTimeout: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/tasktimeout.md)
  The app was terminated for exceeding the allocated time for a background task.
- [static let fileLock: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/filelock.md)
  The app was terminated while suspended for holding file locks.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/terminationcategory-swift.struct)*