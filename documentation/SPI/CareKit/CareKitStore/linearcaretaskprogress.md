---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/linearcaretaskprogress"
framework: "CareKit/CareKitStore"
---

# LinearCareTaskProgress

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A structure that defines user progress for a task that can be completed over time.

## Declaration

```swift
struct LinearCareTaskProgress
```

#### Overview

A progress value updates as a user progresses through the task. When the progress value reaches its goal, the task is considered completed. If there’s no goal, the task is considered completed if the progress value is greater than zero.

This type of progress is useful for tasks such as “Walk 500 steps” or “Exercise for 30 minutes.”

You can easily apply this progress to a user interface element such as a chart or a progress view.

```swift
var body: some View {
    ProgressView(value: progress.fractionCompleted)
}
```

## Topics

### Initializers
- [init(value: Double, goal: Double?)](./linearcaretaskprogress/init%28value,goal%29.md)
  Create a structure that defines user progress for a task that can be completed over time.
### Instance Properties
- [var fractionCompleted: Double](./linearcaretaskprogress/fractioncompleted.md)
- [var goal: Double?](./linearcaretaskprogress/goal.md)
  A value that indicates whether the task is complete.
- [var value: Double](./linearcaretaskprogress/value.md)
  The progress that’s been made towards reaching the goal.
### Default Implementations
- [CareTaskProgress Implementations](./linearcaretaskprogress/caretaskprogress-implementations.md)
- [Equatable Implementations](./linearcaretaskprogress/equatable-implementations.md)

## Relationships

### Conforms To
- [CareTaskProgress](./caretaskprogress.md)
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/linearcaretaskprogress)*