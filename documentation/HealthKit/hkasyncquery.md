# HKAsyncQuery

**Framework**: HealthKit  
**Kind**: protocol

A protocol that defines an asynchronous method for running queries.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
protocol HKAsyncQuery
```

## Mentions

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)

## Topics

### Running Queries
- [associatedtype Output](hkasyncquery/output.md)
  The type of data that the query returns.
- [func result(for: HKHealthStore) async throws -> Self.Output](hkasyncquery/result(for:).md)
  Runs a one-shot query and asynchronously returns a snapshot of the current matching results.

## Relationships

### Conforming Types
- [HKActivitySummaryQueryDescriptor](hkactivitysummaryquerydescriptor.md)
- [HKAnchoredObjectQueryDescriptor](hkanchoredobjectquerydescriptor.md)
- [HKSampleQueryDescriptor](hksamplequerydescriptor.md)
- [HKSourceQueryDescriptor](hksourcequerydescriptor.md)
- [HKStatisticsCollectionQueryDescriptor](hkstatisticscollectionquerydescriptor.md)
- [HKStatisticsQueryDescriptor](hkstatisticsquerydescriptor.md)
- [HKVerifiableClinicalRecordQueryDescriptor](hkverifiableclinicalrecordquerydescriptor.md)
- [HKWorkoutEffortRelationshipQueryDescriptor](hkworkouteffortrelationshipquerydescriptor.md)

## See Also

- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)
  Use Swift concurrency to manage one-shot and long-running queries.
- [protocol HKAsyncSequenceQuery](hkasyncsequencequery.md)
  A protocol that defines a method for running queries that returns results using an asynchronous sequence.
- [struct HKSamplePredicate](hksamplepredicate.md)
  A predicate for queries that return a collection of matching sample objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkasyncquery)*