---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleevent"
framework: "CareKit/CareKitStore"
---

# OCKScheduleEvent

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct OCKScheduleEvent
```

## Topics

### Instance Properties
- [var element: OCKScheduleElement](./ockscheduleevent/element.md)
- [var end: Date](./ockscheduleevent/end.md)
- [var occurrence: Int](./ockscheduleevent/occurrence.md)
- [var start: Date](./ockscheduleevent/start.md)
### Default Implementations
- [Equatable Implementations](./ockscheduleevent/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Events
- [struct OCKEvent](./ockevent.md)
  An event that represents a single occasion that a task was scheduled to occur.
- [struct OCKAnyEvent](./ockanyevent.md)
  A representation of a single occassion which a task was scheduled to occur on.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockscheduleevent)*