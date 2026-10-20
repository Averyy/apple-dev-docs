# result(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Runs a one-shot query and asynchronously returns statistics calculated from the current matching results.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> HKStatisticsCollection
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

### Running Queries
- [func results(for: HKHealthStore) -> HKStatisticsCollectionQueryDescriptor.Results](./results%28for%29.md)
  Initiates a long-running query that returns statistics and updates using an asynchronous sequence.
- [HKStatisticsCollectionQueryDescriptor.Results](./results.md)
  An asynchronous sequence that emits updates from a statistics collection query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/result(for:))*