# result(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Runs a one-shot query and asynchronously returns a snapshot of the current matching results.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> [HKActivitySummary]
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

### Running queries
- [func results(for: HKHealthStore) -> HKActivitySummaryQueryDescriptor.Results](./results%28for%29.md)
  Initiates a long-running query that returns its results using an asynchronous sequence.
- [HKActivitySummaryQueryDescriptor.Results](./results.md)
  An asynchronous sequence that emits updates from an activity summary query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkactivitysummaryquerydescriptor/result(for:))*