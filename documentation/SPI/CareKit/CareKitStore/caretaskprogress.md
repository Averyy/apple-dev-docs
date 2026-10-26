---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogress"
framework: "CareKit/CareKitStore"
---

# CareTaskProgress

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A protocol that describes user progress for a task.

## Declaration

```swift
protocol CareTaskProgress
```

## Topics

### Instance Properties
- [var fractionCompleted: Double](./caretaskprogress/fractioncompleted.md)
  The fraction of the task that completed between 0 and 1 inclusive.
- [var isCompleted: Bool](./caretaskprogress/iscompleted.md)
  A property set to `true` if the task is considered completed.

## Relationships

### Conforming Types
- [AggregatedCareTaskProgress](./aggregatedcaretaskprogress.md)
- [BinaryCareTaskProgress](./binarycaretaskprogress.md)
- [LinearCareTaskProgress](./linearcaretaskprogress.md)

## See Also

### Care task progress
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
- [struct OCKAdherenceQuery](./ockadherencequery.md)
  `OCKAdherenceQuery` is used to constrain the results returned when fetching adherence from a store.
- [enum OCKAdherence](./ockadherence.md)
  `OCKAdherence` specifies how many of their assigned tasks a patient has completed.
- [enum OCKAdherenceAggregator](./ockadherenceaggregator.md)
  An enumerator that specifies a number of methods for computing an adherence value given an array of events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogress)*