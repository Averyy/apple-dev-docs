# result(for:)

**Framework**: HealthKit  
**Kind**: method

Runs a one-shot query and asynchronously returns statistics calculated from the current matching results.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> HKStatisticsCollection
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [func results(for: HKHealthStore) -> HKStatisticsCollectionQueryDescriptor.Results](hkstatisticscollectionquerydescriptor/results(for:).md)
  Initiates a long-running query that returns statistics and updates using an asynchronous sequence.
- [HKStatisticsCollectionQueryDescriptor.Results](hkstatisticscollectionquerydescriptor/results.md)
  An asynchronous sequence that emits updates from a statistics collection query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquerydescriptor/result(for:))*