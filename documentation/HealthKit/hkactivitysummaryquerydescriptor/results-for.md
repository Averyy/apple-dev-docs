# results(for:)

**Framework**: HealthKit  
**Kind**: method

Initiates a long-running query that returns its results using an asynchronous sequence.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func results(for healthStore: HKHealthStore) -> HKActivitySummaryQueryDescriptor.Results
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [func result(for: HKHealthStore) async throws -> [HKActivitySummary]](hkactivitysummaryquerydescriptor/result(for:).md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
- [HKActivitySummaryQueryDescriptor.Results](hkactivitysummaryquerydescriptor/results.md)
  An asynchronous sequence that emits updates from an activity summary query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquerydescriptor/results(for:))*