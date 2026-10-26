---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherenceaggregator"
framework: "CareKit/CareKitStore"
---

# OCKAdherenceAggregator

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

An enumerator that specifies a number of methods for computing an adherence value given an array of events.

## Declaration

```swift
enum OCKAdherenceAggregator
```

## Topics

### Enumeration Cases
- [OCKAdherenceAggregator.compareTargetValues](./ockadherenceaggregator/comparetargetvalues.md)
  Computes a percentage for each event that is either 1.0 or 0.0 depending on if the outcomes values match or exceed the target values. If no target values are specified on the event, then the existence of an outcome will result in a value of 1.0. The average completion across all events will be returned.
- [case custom(([OCKAnyEvent]) -> OCKAdherence)](./ockadherenceaggregator/custom%28_%29.md)
  Specifies a custom closure that operates on a day’s worth of events and returns an adherence value
- [OCKAdherenceAggregator.outcomeExists](./ockadherenceaggregator/outcomeexists.md)
  Computes a percentage by checking if the outcome for each event exists. Any event with a non-nil outcome will be counted as 100% complete, and any event without an outcome will be counted as 0% complete. The average completion across all events will be returned.
- [OCKAdherenceAggregator.percentOfOutcomeValuesThatExist](./ockadherenceaggregator/percentofoutcomevaluesthatexist.md)
  Computes a percentage for each event by dividing the number of outcomes values by the number of expected outcomes values. The average completion across all events will be returned.
- [OCKAdherenceAggregator.percentOfTargetValuesMet](./ockadherenceaggregator/percentoftargetvaluesmet.md)
  Computes an analog percentage for each event as the number of met target values divided by the total number of target goals. The average completion accross all events will be returned.
### Instance Methods
- [func aggregate(events: [OCKAnyEvent]) -> OCKAdherence](./ockadherenceaggregator/aggregate%28events%29.md)
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
- [enum OCKEventAggregator](./ockeventaggregator.md)
  An enumerator that specifies a number of methods for computing a value given an array of events that occurred on some day.
- [struct OCKAdherenceQuery](./ockadherencequery.md)
  `OCKAdherenceQuery` is used to constrain the results returned when fetching adherence from a store.
- [enum OCKAdherence](./ockadherence.md)
  `OCKAdherence` specifies how many of their assigned tasks a patient has completed.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockadherenceaggregator)*