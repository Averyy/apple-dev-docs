---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadonlyeventstore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKReadOnlyEventStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func events(matching: OCKEventQuery) -> CareStoreQueryResults<Event>](./events%28matching%29.md)
- [func fetchEvent(forTask: Task, occurrence: Int) async throws -> Event](./fetchevent%28fortask,occurrence%29.md)
  `fetchEvent` retrieves a single occurrence of the specified task.
- [func fetchEvent(forTask: Self.Task, occurrence: Int, callbackQueue: DispatchQueue, completion: OCKResultClosure<Event>)](./fetchevent%28fortask,occurrence,callbackqueue,completion%29.md)
- [func fetchEvents(query: OCKEventQuery) async throws -> [Event]](./fetchevents%28query%29.md)
  `fetchEvents` retrieves all the occurrences of the specified task in the interval specified by the provided query.
- [func fetchEvents(query: OCKEventQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKEvent<Task, Outcome>]>)](./fetchevents%28query,callbackqueue,completion%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadonlyeventstore-implementations)*