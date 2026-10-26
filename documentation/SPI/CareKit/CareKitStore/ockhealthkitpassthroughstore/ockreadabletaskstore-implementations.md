---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/ockreadabletaskstore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKReadableTaskStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func fetchTask(withID: String) async throws -> Task](./fetchtask%28withid%29.md)
  `fetchTask` asynchronously retrieves an array of tasks from the store using its user-defined unique identifier. If a task with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchTask(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>)](./fetchtask%28withid,callbackqueue,completion%29.md)
- [func fetchTasks(query: OCKTaskQuery) async throws -> [Task]](./fetchtasks%28query%29.md)
  `fetchTasks` asynchronously retrieves an array of tasks from the store.
- [func fetchTasks(query: OCKTaskQuery, callbackQueue: DispatchQueue, completion: @Sendable (Result<[OCKHealthKitTask], OCKStoreError>) -> Void)](./fetchtasks%28query,callbackqueue,completion%29.md)
- [func tasks(matching: OCKTaskQuery) -> CareStoreQueryResults<OCKHealthKitTask>](./tasks%28matching%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/ockreadabletaskstore-implementations)*