# HKAnchoredObjectQueryDescriptor.Result

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

A set of results from an anchored object query.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
struct Result
```

## Topics

### Accessing the Results
- [let addedSamples: [Sample]](./result/addedsamples.md)
  An array containing the matching samples added to the HealthKit store.
- [let deletedObjects: [HKDeletedObject]](./result/deletedobjects.md)
  An array of objects deleted from the HealthKit store.
- [let newAnchor: HKQueryAnchor](./result/newanchor.md)
  A value corresponding to the last sample that the anchor query has returned.

## See Also

### Running Queries
- [func result(for: HKHealthStore) async throws -> HKAnchoredObjectQueryDescriptor<Sample>.Result](./result%28for%29.md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.
- [func results(for: HKHealthStore) -> HKAnchoredObjectQueryDescriptor<Sample>.Results](./results%28for%29.md)
  Initiates a long-running query that returns its results using an asynchronous sequence.
- [HKAnchoredObjectQueryDescriptor.Results](./results.md)
  An asynchronous sequence that emits updates from an anchored object query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquerydescriptor/result)*