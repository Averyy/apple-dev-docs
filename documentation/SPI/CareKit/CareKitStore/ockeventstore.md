---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockeventstore"
framework: "CareKit/CareKitStore"
---

# OCKEventStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store in which a single event type can be both queried and written is considered a `OCKEventStore`.

## Declaration

```swift
protocol OCKEventStore : OCKAnyEventStore, OCKOutcomeStore, OCKReadOnlyEventStore, OCKTaskStore
```

## Relationships

### Inherits From
- [OCKAnyEventStore](./ockanyeventstore.md)
- [OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKAnyTaskStore](./ockanytaskstore.md)
- [OCKOutcomeStore](./ockoutcomestore.md)
- [OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
- [OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
- [OCKReadableTaskStore](./ockreadabletaskstore.md)
- [OCKTaskStore](./ocktaskstore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
- [OCKStore](./ockstore.md)

## See Also

### Events
- [struct OCKEvent](./ockevent.md)
  An event that represents a single occasion that a task was scheduled to occur.
- [struct OCKAnyEvent](./ockanyevent.md)
  A representation of a single occassion which a task was scheduled to occur on.
- [struct OCKScheduleEvent](./ockscheduleevent.md)
- [protocol OCKAnyEventStore](./ockanyeventstore.md)
  Any store from which `OCKAnyEvent`s  can be queried and also written is considered `OCKAnyEventStore`.
- [protocol OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
  A store that allows for reading events.
- [protocol OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
  A store that allows for reading events.
- [struct OCKEventQuery](./ockeventquery.md)
  A query that limits which events will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockeventstore)*