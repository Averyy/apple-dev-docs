# HKAsyncSequenceQuery

**Framework**: HealthKit  
**Kind**: protocol

A protocol that defines a method for running queries that returns results using an asynchronous sequence.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
protocol HKAsyncSequenceQuery
```

## Mentions

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)

## Topics

### Running Queries
- [associatedtype Sequence : AsyncSequence](hkasyncsequencequery/sequence.md)
  The data type that the query returns.
- [func results(for: HKHealthStore) -> Self.Sequence](hkasyncsequencequery/results(for:).md)
  Initiates a query that returns its results using an asynchronous sequence.

## Relationships

### Conforming Types
- [HKActivitySummaryQueryDescriptor](hkactivitysummaryquerydescriptor.md)
- [HKAnchoredObjectQueryDescriptor](hkanchoredobjectquerydescriptor.md)
- [HKElectrocardiogramQueryDescriptor](hkelectrocardiogramquerydescriptor.md)
- [HKHeartbeatSeriesQueryDescriptor](hkheartbeatseriesquerydescriptor.md)
- [HKQuantitySeriesSampleQueryDescriptor](hkquantityseriessamplequerydescriptor.md)
- [HKStatisticsCollectionQueryDescriptor](hkstatisticscollectionquerydescriptor.md)
- [HKWorkoutEffortRelationshipQueryDescriptor](hkworkouteffortrelationshipquerydescriptor.md)
- [HKWorkoutRouteQueryDescriptor](hkworkoutroutequerydescriptor.md)

## See Also

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)
  Use Swift concurrency to manage one-shot and long-running queries.
- [protocol HKAsyncQuery](hkasyncquery.md)
  A protocol that defines an asynchronous method for running queries.
- [struct HKSamplePredicate](hksamplepredicate.md)
  A predicate for queries that return a collection of matching sample objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkasyncsequencequery)*