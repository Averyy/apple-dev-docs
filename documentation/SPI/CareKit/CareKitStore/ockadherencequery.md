---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherencequery"
framework: "CareKit/CareKitStore"
---

# OCKAdherenceQuery

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

`OCKAdherenceQuery` is used to constrain the results returned when fetching adherence from a store.

## Declaration

```swift
struct OCKAdherenceQuery
```

## Topics

### Initializers
- [init(taskIDs: [String], dateInterval: DateInterval, aggregator: OCKAdherenceAggregator)](./ockadherencequery/init%28taskids,dateinterval,aggregator%29.md)
  Initialize a new query by specifying the taskIDs, dates, and aggregator.
- [init(taskIDs: [String], dateInterval: DateInterval, computeProgress: @Sendable (OCKAnyEvent) -> CareTaskProgress)](./ockadherencequery/init%28taskids,dateinterval,computeprogress%29.md)
  Initialize a new query by specifying the taskIDs, dates, and aggregator.
### Instance Properties
- [var dateInterval: DateInterval](./ockadherencequery/dateinterval.md)
  The date interval for which to return adherence information.
- [var taskIDs: [String]](./ockadherencequery/taskids.md)
  The IDs of the tasks for which adherence should be calculated.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Care task progress
- [protocol CareTaskProgress](./caretaskprogress.md)
  A protocol that describes user progress for a task.
- [struct CareTaskProgressStrategy](./caretaskprogressstrategy.md)
  A structure that provides access to various strategies for computing progress for a task.
- [struct BinaryCareTaskProgress](./binarycaretaskprogress.md)
  User progress for a task that is either completed or incomplete.
- [struct LinearCareTaskProgress](./linearcaretaskprogress.md)
  A structure that defines user progress for a task that can be completed over time.
- [struct AggregatedCareTaskProgress](./aggregatedcaretaskprogress.md)
  An object that combines the progress for multiple tasks.
- [enum OCKEventAggregator](./ockeventaggregator.md)
  An enumerator that specifies a number of methods for computing a value given an array of events that occurred on some day.
- [enum OCKAdherence](./ockadherence.md)
  `OCKAdherence` specifies how many of their assigned tasks a patient has completed.
- [enum OCKAdherenceAggregator](./ockadherenceaggregator.md)
  An enumerator that specifies a number of methods for computing an adherence value given an array of events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherencequery)*