---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockanyreadonlyeventstore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKAnyReadOnlyEventStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func anyEvents(matching: OCKEventQuery) -> CareStoreQueryResults<OCKAnyEvent>](./anyevents%28matching%29.md)
- [func fetchAdherence(query: OCKAdherenceQuery) async throws -> [OCKAdherence]](./fetchadherence%28query%29.md)
  `fetchAdherence` retrieves all the events and calculates the percent of tasks completed for every day between two dates.
- [func fetchAdherence(query: OCKAdherenceQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAdherence]>)](./fetchadherence%28query,callbackqueue,completion%29.md)
- [func fetchAnyEvent(forTask: OCKAnyTask, occurrence: Int) async throws -> OCKAnyEvent](./fetchanyevent%28fortask,occurrence%29.md)
  `fetchAnyEvent` retrieves a single occurrence of the specified task.
- [func fetchAnyEvent(forTask: OCKAnyTask, occurrence: Int, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyEvent>)](./fetchanyevent%28fortask,occurrence,callbackqueue,completion%29.md)
- [func fetchAnyEvents(query: OCKEventQuery) async throws -> [OCKAnyEvent]](./fetchanyevents%28query%29.md)
  `fetchAnyEvents` retrieves all the occurrences of the specified task in the interval specified by the provided query.
- [func fetchAnyEvents(query: OCKEventQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyEvent]>)](./fetchanyevents%28query,callbackqueue,completion%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockanyreadonlyeventstore-implementations)*