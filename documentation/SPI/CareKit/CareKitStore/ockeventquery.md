---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockeventquery"
framework: "CareKit/CareKitStore"
---

# OCKEventQuery

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A query that limits which events will be returned when fetching.

## Declaration

```swift
struct OCKEventQuery
```

## Topics

### Initializers
- [init(dateInterval: DateInterval)](./ockeventquery/init%28dateinterval%29.md)
  Initialize a new `OCKEventQuery` by specifying the start and end dates.
- [init(for: Date)](./ockeventquery/init%28for%29.md)
  Initialize a new `OCKEventQuery` by specifying a particular date.
### Instance Properties
- [var dateInterval: DateInterval](./ockeventquery/dateinterval.md)
  The date interval in which events should be returned.
- [var taskGroupIdentifiers: [String]](./ockeventquery/taskgroupidentifiers.md)
  The group identifiers of tasks to match events against.
- [var taskIDs: [String]](./ockeventquery/taskids.md)
  The identifiers of tasks to match events against.
- [var taskTags: [String]](./ockeventquery/tasktags.md)
  The tags of tasks to match events against.
### Default Implementations
- [Equatable Implementations](./ockeventquery/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Events
- [struct OCKEvent](./ockevent.md)
  An event that represents a single occasion that a task was scheduled to occur.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockeventquery)*