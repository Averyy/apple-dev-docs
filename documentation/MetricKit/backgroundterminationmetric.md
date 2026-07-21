# BackgroundTerminationMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that counts app terminations from the background by category.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct BackgroundTerminationMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.backgroundTermination(_:)`](metricresult/backgroundtermination(_:).md) case. It appears in both [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md) when state reporting is enabled.

Use [`terminationCategory`](crashdiagnostic/terminationcategory-swift.property.md) to correlate individual crash diagnostics with these aggregate counts.

Unexpected background terminations can affect downstream performance metrics such as launch time, because the app must fully restart instead of resuming from suspension. For information about launch times when the app resumes from suspension, see [`ApplicationResumeTimeMetric`](applicationresumetimemetric.md).

## Topics

### Background termination counts
- [let normalTerminationCount: Int](backgroundterminationmetric/normalterminationcount.md)
  The number of times the application terminated normally from the background.
- [let memoryLimitTerminationCount: Int](backgroundterminationmetric/memorylimitterminationcount.md)
  The number of times the system terminated the app from the background for using too much memory.
- [let highCPUTerminationCount: Int](backgroundterminationmetric/highcputerminationcount.md)
  The number of times the system terminated the app from the background for using too much CPU time.
- [let systemPressureTerminationCount: Int](backgroundterminationmetric/systempressureterminationcount.md)
  The number of times the system terminated the app from the background to free up memory.
- [let badAccessTerminationCount: Int](backgroundterminationmetric/badaccessterminationcount.md)
  The number of times the system terminated the app from the background for attempting an invalid memory access.
- [let abnormalTerminationCount: Int](backgroundterminationmetric/abnormalterminationcount.md)
  The number of times the app terminated abnormally from the background.
- [let illegalInstructionTerminationCount: Int](backgroundterminationmetric/illegalinstructionterminationcount.md)
  The number of times the system terminated the app from the background for attempting to execute an illegal or undefined instruction.
- [let watchdogTerminationCount: Int](backgroundterminationmetric/watchdogterminationcount.md)
  The number of times the system watchdog terminated the app from the background.
- [let fileLockTerminationCount: Int](backgroundterminationmetric/filelockterminationcount.md)
  The number of times the system terminated the app from the background while being suspended and having file locks.
- [let taskTimeoutTerminationCount: Int](backgroundterminationmetric/tasktimeoutterminationcount.md)
  The number of times the system terminated the app from the background for exceeding the allocated time for a background task.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ForegroundTerminationMetric](foregroundterminationmetric.md)
  A metric that counts app terminations from the foreground by category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/backgroundterminationmetric)*