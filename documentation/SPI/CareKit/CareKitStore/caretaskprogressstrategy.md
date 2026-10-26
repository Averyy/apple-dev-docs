---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogressstrategy"
framework: "CareKit/CareKitStore"
---

# CareTaskProgressStrategy

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A structure that provides access to various strategies for computing progress for a task.

## Declaration

```swift
struct CareTaskProgressStrategy<Progress> where Progress : CareTaskProgress
```

#### Overview

This structure is most commonly used when you already have access to an event and want to specify a strategy for computing progress:

```swift
let steps: OCKAnyEvent = getStepsEvent()
let stepsProgress = steps.computeProgress(by: .summingOutcomeValues)
```

To create your own progress computation strategy, start by defining a data structure that stores task progress. The data structure should conform to [`CareTaskProgress`](./caretaskprogress.md).

```swift
struct PhysicalTherapyProgress: CareTaskProgress {

    // Custom properties here...

    // Required by `CareTaskProgress`
    var fractionCompleted: Double
}
```

Next, extend [`CareTaskProgressStrategy`](./caretaskprogressstrategy.md) and write out logic for computing the custom progress for a task.

```swift
extension CareTaskProgressStrategy {

    public static var customStrategy: CareTaskProgressStrategy<PhysicalTherapyProgress> {

        return CareTaskProgressStrategy<PhysicalTherapyProgress> { event in
            return computeCustomProgress(for: event)
        }

    }
}
```

Now you can acess the strategy just like the other strategies in the framework.

```swift

// Custom strategy.
let physicalTherapy: OCKAnyEvent = getPhysicalTherapyEvent()
let physicalTherapyProgress = physicalTherapy.computeProgress(by: .customStrategy)

// Default strategy.
let steps: OCKAnyEvent = getStepsEvent()
let stepsProgress = steps.computeProgress(by: .summingOutcomeValues)

// You can aggregate both default and custom progress data structures.
let progress = AggregatedCareTaskProgress(combining: [stepsProgress, physicalTherapyProgress]
```

## Topics

### Initializers
- [init(computeProgress: (OCKAnyEvent) -> Progress)](./caretaskprogressstrategy/init%28computeprogress%29.md)
  Create a custom task progress computation strategy.
### Type Properties
- [static var checkingOutcomeExists: CareTaskProgressStrategy<BinaryCareTaskProgress>](./caretaskprogressstrategy/checkingoutcomeexists.md)
  A strategy that computes progress for a task by checking for the existence of an outcome.
- [static var summingOutcomeValues: CareTaskProgressStrategy<LinearCareTaskProgress>](./caretaskprogressstrategy/summingoutcomevalues.md)
  A strategy that computes progress for a task.

## See Also

### Care task progress
- [protocol CareTaskProgress](./caretaskprogress.md)
  A protocol that describes user progress for a task.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/caretaskprogressstrategy)*