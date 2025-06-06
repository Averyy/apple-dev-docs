# result(for:)

**Framework**: HealthKit  
**Kind**: method

Runs a one-shot query and asynchronously returns a snapshot of the current matching results.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> [HKActivitySummary]
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [func results(for: HKHealthStore) -> HKActivitySummaryQueryDescriptor.Results](hkactivitysummaryquerydescriptor/results(for:).md)
  Initiates a long-running query that returns its results using an asynchronous sequence.
- [HKActivitySummaryQueryDescriptor.Results](hkactivitysummaryquerydescriptor/results.md)
  An asynchronous sequence that emits updates from an activity summary query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquerydescriptor/result(for:))*