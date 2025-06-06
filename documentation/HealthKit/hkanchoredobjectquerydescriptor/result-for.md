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
func result(for healthStore: HKHealthStore) async throws -> HKAnchoredObjectQueryDescriptor<Sample>.Result
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [func results(for: HKHealthStore) -> HKAnchoredObjectQueryDescriptor<Sample>.Results](hkanchoredobjectquerydescriptor/results(for:).md)
  Initiates a long-running query that returns its results using an asynchronous sequence.
- [HKAnchoredObjectQueryDescriptor.Result](hkanchoredobjectquerydescriptor/result.md)
  A set of results from an anchored object query.
- [HKAnchoredObjectQueryDescriptor.Results](hkanchoredobjectquerydescriptor/results.md)
  An asynchronous sequence that emits updates from an anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/result(for:))*