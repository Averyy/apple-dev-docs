---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/aggregatedcaretaskprogress"
framework: "CareKit/CareKitStore"
---

# AggregatedCareTaskProgress

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An object that combines the progress for multiple tasks.

## Declaration

```swift
struct AggregatedCareTaskProgress
```

#### Overview

This type can be useful for displaying progress for multiple tasks using a progress bar. If you have multiple events, start by computing the progress for each event individually:

```swift
let medication: OCKAnyEvent = getMedicationEvent()
let medicationProgress = medication.computeProgress(by: .checkingOutcomeExists)

let steps: OCKAnyEvent = getStepsEvent()
let stepsProgress = steps.computeProgress(by: .summingOutcomeValues)

let progress = AggregatedCareTaskProgress(combining: [medicationProgress, stepsProgress]
```

Progress units are weighted equally when combining progress for multiple events. In the example above, suppose each of the two events is 50% completed. The final combined progress becomes 50%. Now suppose one event is 100% completed and the other is 50% completed. The final progress becomes 75%.

Use this type to create parent progress for a group of subtasks:

```swift
let medicationDoseA: OCKAnyEvent = getDoseAEvent()
let medicationDoseB: OCKAnyEvent = getDoseBEvent()
let medicationProgress = AggregatedCareTaskProgress(events: [medicationDoseA, medicationDoseB])

let steps: OCKAnyEvent = getStepsEvent()
let stepsProgress = steps.computeProgress(by: .summingOutcomeValues)

let progress = AggregatedCareTaskProgress(combining: [medicationProgress, stepsProgress]
```

Once progress is constructed, it can easily be applied to a [ProgressView](https://developer.apple.com/documentation/swiftui/progressview) in SwiftUI:

```swift
var body: some View {
    ProgressView(value: progress.fractionCompleted)
}
```

## Topics

### Initializers
- [init(combining: [CareTaskProgress])](./aggregatedcaretaskprogress/init%28combining%29.md)
  Create user progress by combining the progress for multiple tasks.
- [init<Progress>(events: [OCKAnyEvent], by: CareTaskProgressStrategy<Progress>)](./aggregatedcaretaskprogress/init%28events,by%29.md)
  Create user progress by computing and combining the progress for multiple tasks using a single strategy.
### Instance Properties
- [let fractionCompleted: Double](./aggregatedcaretaskprogress/fractioncompleted.md)
### Default Implementations
- [CareTaskProgress Implementations](./aggregatedcaretaskprogress/caretaskprogress-implementations.md)
- [Equatable Implementations](./aggregatedcaretaskprogress/equatable-implementations.md)

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
- [struct LinearCareTaskProgress](./linearcaretaskprogress.md)
  A structure that defines user progress for a task that can be completed over time.
- [enum OCKEventAggregator](./ockeventaggregator.md)
  An enumerator that specifies a number of methods for computing a value given an array of events that occurred on some day.
- [struct OCKAdherenceQuery](./ockadherencequery.md)
  `OCKAdherenceQuery` is used to constrain the results returned when fetching adherence from a store.
- [enum OCKAdherence](./ockadherence.md)
  `OCKAdherence` specifies how many of their assigned tasks a patient has completed.
- [enum OCKAdherenceAggregator](./ockadherenceaggregator.md)
  An enumerator that specifies a number of methods for computing an adherence value given an array of events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/aggregatedcaretaskprogress)*