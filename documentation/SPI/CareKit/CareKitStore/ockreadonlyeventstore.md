---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadonlyeventstore"
framework: "CareKit/CareKitStore"
---

# OCKReadOnlyEventStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading events.

## Declaration

```swift
protocol OCKReadOnlyEventStore : OCKAnyReadOnlyEventStore, OCKReadableOutcomeStore, OCKReadableTaskStore
```

## Topics

### Associated Types
- [associatedtype Events : Sendable, AsyncSequence](./ockreadonlyeventstore/events.md)
  An asynchronous sequence that produces events.
### Instance Methods
- [func events(matching: OCKEventQuery) -> Events](./ockreadonlyeventstore/events%28matching%29.md)
  A continuous stream of events (occurrences of tasks) that exist in the store.
- [func fetchEvent(forTask: Task, occurrence: Int) async throws -> Event](./ockreadonlyeventstore/fetchevent%28fortask,occurrence%29.md)
  `fetchEvent` retrieves a single occurrence of the specified task.
- [func fetchEvent(forTask: Task, occurrence: Int, callbackQueue: DispatchQueue, completion: OCKResultClosure<Event>)](./ockreadonlyeventstore/fetchevent%28fortask,occurrence,callbackqueue,completion%29.md)
  `fetchEvent` retrieves a single occurrence of the specified task.
- [func fetchEvents(query: OCKEventQuery) async throws -> [Event]](./ockreadonlyeventstore/fetchevents%28query%29.md)
  `fetchEvents` retrieves all the occurrences of the specified task in the interval specified by the provided query.
- [func fetchEvents(query: OCKEventQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[Event]>)](./ockreadonlyeventstore/fetchevents%28query,callbackqueue,completion%29.md)
  The completion will be called with an error if there’s an issue accessing the store or fetching results.
### Type Aliases
- [OCKReadOnlyEventStore.Event](./ockreadonlyeventstore/event.md)

## Relationships

### Inherits From
- [OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
- [OCKReadableTaskStore](./ockreadabletaskstore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKEventStore](./ockeventstore.md)
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
- [protocol OCKEventStore](./ockeventstore.md)
  Any store in which a single event type can be both queried and written is considered a `OCKEventStore`.
- [protocol OCKAnyEventStore](./ockanyeventstore.md)
  Any store from which `OCKAnyEvent`s  can be queried and also written is considered `OCKAnyEventStore`.
- [protocol OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
  A store that allows for reading events.
- [struct OCKEventQuery](./ockeventquery.md)
  A query that limits which events will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadonlyeventstore)*