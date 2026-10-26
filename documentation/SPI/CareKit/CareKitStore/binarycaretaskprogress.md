---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/binarycaretaskprogress"
framework: "CareKit/CareKitStore"
---

# BinaryCareTaskProgress

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

User progress for a task that is either completed or incomplete.

## Declaration

```swift
struct BinaryCareTaskProgress
```

#### Overview

This type of progress can be useful for tasks such as “Take a medication” or “Stretch your back.”

Once progress is constructed, it can easily be applied to a [ProgressView](https://developer.apple.com/documentation/swiftui/progressview) in SwiftUI:

```swift
var body: some View {
    ProgressView(value: progress.fractionCompleted)
}
```

## Topics

### Initializers
- [init(isCompleted: Bool)](./binarycaretaskprogress/init%28iscompleted%29.md)
  Create user progress for a task that is either completed or incomplete.
### Instance Properties
- [var fractionCompleted: Double](./binarycaretaskprogress/fractioncompleted.md)
- [var isCompleted: Bool](./binarycaretaskprogress/iscompleted.md)
  True if the task is considered completed.
### Default Implementations
- [Equatable Implementations](./binarycaretaskprogress/equatable-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/binarycaretaskprogress)*