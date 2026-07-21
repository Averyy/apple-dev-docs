# ForegroundTerminationMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that counts app terminations from the foreground by category.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct ForegroundTerminationMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.foregroundTermination(_:)`](metricresult/foregroundtermination(_:).md) case. It appears in both [`intervalEntries`](metricreport/intervalentries.md) and [`stateEntries`](metricreport/stateentries.md) when state reporting is enabled.

Foreground exits are user-visible terminations; when unexpected, they directly interrupt usage. Not all exits are unexpected — normal exits such as the user quitting the app from the switcher appear in [`normalTerminationCount`](foregroundterminationmetric/normalterminationcount.md).

Use [`terminationCategory`](crashdiagnostic/terminationcategory-swift.property.md) to correlate individual crash diagnostics with these aggregate counts.

## Topics

### Foreground termination counts
- [let normalTerminationCount: Int](foregroundterminationmetric/normalterminationcount.md)
  The number of times the application terminated normally from the foreground.
- [let memoryLimitTerminationCount: Int](foregroundterminationmetric/memorylimitterminationcount.md)
  The number of times the system terminated the app from the foreground for using too much memory.
- [let badAccessTerminationCount: Int](foregroundterminationmetric/badaccessterminationcount.md)
  The number of times the system terminated the app from the foreground for attempting an invalid memory access.
- [let abnormalTerminationCount: Int](foregroundterminationmetric/abnormalterminationcount.md)
  The number of times the app terminated abnormally from the foreground.
- [let illegalInstructionTerminationCount: Int](foregroundterminationmetric/illegalinstructionterminationcount.md)
  The number of times the system terminated the app from the foreground for attempting to execute an illegal or undefined instruction.
- [let watchdogTerminationCount: Int](foregroundterminationmetric/watchdogterminationcount.md)
  The number of times the system watchdog terminated the app from the foreground.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct BackgroundTerminationMetric](backgroundterminationmetric.md)
  A metric that counts app terminations from the background by category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/foregroundterminationmetric)*