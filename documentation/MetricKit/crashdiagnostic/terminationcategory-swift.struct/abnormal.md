# abnormal

**Framework**: MetricKit  
**Kind**: property

The app terminated abnormally, typically due to an uncaught exception or call to `abort()`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let abnormal: CrashDiagnostic.TerminationCategory
```

#### Discussion

Corresponds to [`abnormalTerminationCount`](foregroundterminationmetric/abnormalterminationcount.md) and [`abnormalTerminationCount`](backgroundterminationmetric/abnormalterminationcount.md).

## See Also

- [static let badAccess: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/badaccess.md)
  The app was terminated for attempting an invalid memory access.
- [static let illegalInstruction: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/illegalinstruction.md)
  The app was terminated for executing an illegal or undefined instruction.
- [static let watchdog: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/watchdog.md)
  The app was terminated by the system watchdog for failing to respond in time.
- [static let taskTimeout: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/tasktimeout.md)
  The app was terminated for exceeding the allocated time for a background task.
- [static let fileLock: CrashDiagnostic.TerminationCategory](crashdiagnostic/terminationcategory-swift.struct/filelock.md)
  The app was terminated while suspended for holding file locks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/terminationcategory-swift.struct/abnormal)*