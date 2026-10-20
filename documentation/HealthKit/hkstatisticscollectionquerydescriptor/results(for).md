# results(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Initiates a long-running query that returns statistics and updates using an asynchronous sequence.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
func results(for healthStore: HKHealthStore) -> HKStatisticsCollectionQueryDescriptor.Results
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

### Running Queries
- [func result(for: HKHealthStore) async throws -> HKStatisticsCollection](./result%28for%29.md)
  Runs a one-shot query and asynchronously returns statistics calculated from the current matching results.
- [HKStatisticsCollectionQueryDescriptor.Results](./results.md)
  An asynchronous sequence that emits updates from a statistics collection query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/results(for:))*