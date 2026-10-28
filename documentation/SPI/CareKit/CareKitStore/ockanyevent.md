---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyevent"
framework: "CareKit/CareKitStore"
---

# OCKAnyEvent

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A representation of a single occassion which a task was scheduled to occur on.

## Declaration

```swift
struct OCKAnyEvent
```

## Overview

The event contains a copy of the task itself, as well as the schedule event and an outcome that is non-`nil` if progress occurred on the task.

## Topics

### Initializers
- [init(task: OCKAnyTask, outcome: OCKAnyOutcome?, scheduleEvent: OCKScheduleEvent)](./ockanyevent/init%28task,outcome,scheduleevent%29.md)
  Creates an event with a task, schedule event, and optional outcome.
### Instance Properties
- [let id: String](./ockanyevent/id.md)
  The stable identifier that can be used for the `Identifiable` protocol.
- [let outcome: OCKAnyOutcome?](./ockanyevent/outcome.md)
  The outcome for this event.
- [let scheduleEvent: OCKScheduleEvent](./ockanyevent/scheduleevent.md)
  The schedule event for this task occurrence.
- [let task: OCKAnyTask](./ockanyevent/task.md)
  The task that this event is associated with.
### Instance Methods
- [func computeProgress<Progress>(by: CareTaskProgressStrategy<Progress>) -> Progress](./ockanyevent/computeprogress%28by%29.md)
  Compute the progress for an event.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Events
- [struct OCKEvent](./ockevent.md)
  An event that represents a single occasion that a task was scheduled to occur.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyevent)*