---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyeventstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyReadOnlyEventStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading events.

## Declaration

```swift
protocol OCKAnyReadOnlyEventStore : OCKAnyReadOnlyOutcomeStore, OCKAnyReadOnlyTaskStore
```

## Topics

### Instance Methods
- [func anyEvents(matching: OCKEventQuery) -> CareStoreQueryResults<OCKAnyEvent>](./ockanyreadonlyeventstore/anyevents%28matching%29.md)
  A continuous stream of events (occurrences of tasks) that exist in the store.
- [func fetchAdherence(query: OCKAdherenceQuery) async throws -> [OCKAdherence]](./ockanyreadonlyeventstore/fetchadherence%28query%29.md)
  `fetchAdherence` retrieves all the events and calculates the percent of tasks completed for every day between two dates.
- [func fetchAdherence(query: OCKAdherenceQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAdherence]>)](./ockanyreadonlyeventstore/fetchadherence%28query,callbackqueue,completion%29.md)
  `fetchAdherence` retrieves all the events and calculates the percent of tasks completed for every day between two dates.
- [func fetchAnyEvent(forTask: OCKAnyTask, occurrence: Int) async throws -> OCKAnyEvent](./ockanyreadonlyeventstore/fetchanyevent%28fortask,occurrence%29.md)
  `fetchAnyEvent` retrieves a single occurrence of the specified task.
- [func fetchAnyEvent(forTask: OCKAnyTask, occurrence: Int, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyEvent>)](./ockanyreadonlyeventstore/fetchanyevent%28fortask,occurrence,callbackqueue,completion%29.md)
  `fetchAnyEvent` retrieves the occurrence of the specified task.
- [func fetchAnyEvents(query: OCKEventQuery) async throws -> [OCKAnyEvent]](./ockanyreadonlyeventstore/fetchanyevents%28query%29.md)
  `fetchAnyEvents` retrieves all the occurrences of the specified task in the interval specified by the provided query.
- [func fetchAnyEvents(query: OCKEventQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyEvent]>)](./ockanyreadonlyeventstore/fetchanyevents%28query,callbackqueue,completion%29.md)
  Fetch a list of events that exist in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyEventStore](./ockanyeventstore.md)
- [OCKEventStore](./ockeventstore.md)
- [OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
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
- [protocol OCKAnyEventStore](./ockanyeventstore.md)
  Any store from which `OCKAnyEvent`s  can be queried and also written is considered `OCKAnyEventStore`.
- [protocol OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
  A store that allows for reading events.
- [struct OCKEventQuery](./ockeventquery.md)
  A query that limits which events will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyeventstore)*