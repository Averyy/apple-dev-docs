---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/ockanyreadonlytaskstore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKAnyReadOnlyTaskStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func anyTasks(matching: OCKTaskQuery) -> CareStoreQueryResults<OCKAnyTask>](./anytasks%28matching%29.md)
- [func fetchAnyTask(withID: String) async throws -> OCKAnyTask](./fetchanytask%28withid%29.md)
  Asynchronously retrieve an array of tasks from the store using its user-defined unique identifier.
- [func fetchAnyTask(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyTask>)](./fetchanytask%28withid,callbackqueue,completion%29.md)
- [func fetchAnyTasks(query: OCKTaskQuery) async throws -> [OCKAnyTask]](./fetchanytasks%28query%29.md)
  Asynchronously retrieve an array of tasks from the store.
- [func fetchAnyTasks(query: OCKTaskQuery, callbackQueue: DispatchQueue, completion: @Sendable (Result<[OCKAnyTask], OCKStoreError>) -> Void)](./fetchanytasks%28query,callbackqueue,completion%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/ockanyreadonlytaskstore-implementations)*