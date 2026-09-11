# terminationCategory

**Framework**: MetricKit  
**Kind**: property

The category of termination that caused this crash.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let terminationCategory: CrashDiagnostic.TerminationCategory?
```

#### Discussion

This value corresponds to the termination categories reported by [`ForegroundTerminationMetric`](foregroundterminationmetric.md) and [`BackgroundTerminationMetric`](backgroundterminationmetric.md), enabling correlation between individual crash diagnostics and aggregate termination counts.

This property is `nil` when the termination category cannot be determined from the available crash metadata.

## See Also

- [let terminationReason: CrashDiagnostic.TerminationReason?](crashdiagnostic/terminationreason-swift.property.md)
  The reason the app was terminated as a human-readable string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/terminationcategory-swift.property)*