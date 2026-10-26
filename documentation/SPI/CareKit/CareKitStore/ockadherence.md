---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherence"
framework: "CareKit/CareKitStore"
---

# OCKAdherence

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

`OCKAdherence` specifies how many of their assigned tasks a patient has completed.

## Declaration

```swift
enum OCKAdherence
```

## Topics

### Enumeration Cases
- [OCKAdherence.noEvents](./ockadherence/noevents.md)
  Indicates that tasks were scheduled, but there were no events during the interval in which adherence was computed.
- [OCKAdherence.noTasks](./ockadherence/notasks.md)
  Indicates that there were no tasks scheduled anytime during the interval in which adherence was computed.
- [OCKAdherence.progress(_:)](./ockadherence/progress%28_%29.md)
  Indicates that events were found with specified progress.
### Default Implementations
- [Equatable Implementations](./ockadherence/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
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
- [struct OCKAdherenceQuery](./ockadherencequery.md)
  `OCKAdherenceQuery` is used to constrain the results returned when fetching adherence from a store.
- [enum OCKAdherenceAggregator](./ockadherenceaggregator.md)
  An enumerator that specifies a number of methods for computing an adherence value given an array of events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherence)*