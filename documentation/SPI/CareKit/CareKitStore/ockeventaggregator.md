---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockeventaggregator"
framework: "CareKit/CareKitStore"
---

# OCKEventAggregator

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

An enumerator that specifies a number of methods for computing a value given an array of events that occurred on some day.

## Declaration

```swift
enum OCKEventAggregator
```

## Topics

### Enumeration Cases
- [OCKEventAggregator.countOutcomeValues](./ockeventaggregator/countoutcomevalues.md)
  Counts the total number of outcome values in the entire array of events.
- [OCKEventAggregator.countOutcomes](./ockeventaggregator/countoutcomes.md)
  Count the total number of outcomes in the entire array of events.
- [case custom(([OCKAnyEvent]) -> Double)](./ockeventaggregator/custom%28_%29.md)
  Custom logic that operates a day’s worth of events and returns a y-axis value.
### Instance Methods
- [func aggregate(events: [OCKAnyEvent]) -> Double](./ockeventaggregator/aggregate%28events%29.md)
  Aggregates an array of events into an adherence score.

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
- [struct OCKAdherenceQuery](./ockadherencequery.md)
  `OCKAdherenceQuery` is used to constrain the results returned when fetching adherence from a store.
- [enum OCKAdherence](./ockadherence.md)
  `OCKAdherence` specifies how many of their assigned tasks a patient has completed.
- [enum OCKAdherenceAggregator](./ockadherenceaggregator.md)
  An enumerator that specifies a number of methods for computing an adherence value given an array of events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockeventaggregator)*