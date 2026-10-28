---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockevent"
framework: "CareKit/CareKitStore"
---

# OCKEvent

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An event that represents a single occasion that a task was scheduled to occur.

## Declaration

```swift
struct OCKEvent<Task, Outcome> where Task : OCKAnyTask, Task : Equatable, Outcome : OCKAnyOutcome, Outcome : Equatable
```

## Overview

The event contains a copy of the task itself, the schedule event, and an outcome that’s non-`nil` if progress is made on the task.

## Topics

### Operators
- [static func < (`Self`, `Self`) -> Bool](./ockevent/op%28_,_%29.md)
### Initializers
- [init(task: Task, outcome: Outcome?, scheduleEvent: OCKScheduleEvent)](./ockevent/init%28task,outcome,scheduleevent%29.md)
  Initialize an event with a task, optional outcome, and schedule event.
### Instance Properties
- [let id: String](./ockevent/id.md)
  The stable identifier to use.
- [var outcome: Outcome?](./ockevent/outcome.md)
  A fully typed version of the outcome associated with this event.
- [let scheduleEvent: OCKScheduleEvent](./ockevent/scheduleevent.md)
  A value containing scheduling information for this event.
- [let task: Task](./ockevent/task.md)
  A fully typed version of the task associated with this event.
### Instance Methods
- [func computeProgress<Progress>(by: CareTaskProgressStrategy<Progress>) -> Progress](./ockevent/computeprogress%28by%29.md)
  Compute the progress for an event.
### Default Implementations
- [Comparable Implementations](./ockevent/comparable-implementations.md)
- [Equatable Implementations](./ockevent/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Comparable
- Swift.Equatable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Events
- [struct OCKAnyEvent](./ockanyevent.md)
  A representation of a single occassion which a task was scheduled to occur on.
- [struct OCKScheduleEvent](./ockscheduleevent.md)
- [protocol OCKEventStore](./ockeventstore.md)
  Any store in which a single event type can be both queried and written is considered a `OCKEventStore`.
- [protocol OCKAnyEventStore](./ockanyeventstore.md)
  Any store from which `OCKAnyEvent`s  can be queried and also written is considered `OCKAnyEventStore`.
- [protocol OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
  A store that allows for reading events.
- [protocol OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
  A store that allows for reading events.
- [struct OCKEventQuery](./ockeventquery.md)
  A query that limits which events will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockevent)*