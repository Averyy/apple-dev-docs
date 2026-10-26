---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyeventstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyEventStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store from which `OCKAnyEvent`s  can be queried and also written is considered `OCKAnyEventStore`.

## Declaration

```swift
protocol OCKAnyEventStore : OCKAnyOutcomeStore, OCKAnyReadOnlyEventStore, OCKAnyTaskStore
```

## Relationships

### Inherits From
- [OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKAnyTaskStore](./ockanytaskstore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKEventStore](./ockeventstore.md)
### Conforming Types
- [OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

## See Also

### Events
- [struct OCKEvent](./ockevent.md)
  An event that represents a single occasion that a task was scheduled to occur.
- [struct OCKAnyEvent](./ockanyevent.md)
  A representation of a single occassion which a task was scheduled to occur on.
- [struct OCKScheduleEvent](./ockscheduleevent.md)
- [protocol OCKEventStore](./ockeventstore.md)
  Any store in which a single event type can be both queried and written is considered a `OCKEventStore`.
- [protocol OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
  A store that allows for reading events.
- [protocol OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
  A store that allows for reading events.
- [struct OCKEventQuery](./ockeventquery.md)
  A query that limits which events will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyeventstore)*