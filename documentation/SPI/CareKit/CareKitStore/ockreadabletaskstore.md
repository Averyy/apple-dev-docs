---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore"
framework: "CareKit/CareKitStore"
---

# OCKReadableTaskStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading tasks.

## Declaration

```swift
protocol OCKReadableTaskStore : OCKAnyReadOnlyTaskStore
```

## Topics

### Associated Types
- [associatedtype Task : OCKAnyTask, Equatable](./ockreadabletaskstore/task.md)
- [associatedtype Tasks : Sendable, AsyncSequence](./ockreadabletaskstore/tasks.md)
  An asynchronous sequence that produces tasks.
### Instance Methods
- [func fetchTask(withID: String) async throws -> Task](./ockreadabletaskstore/fetchtask%28withid%29.md)
  `fetchTask` asynchronously retrieves an array of tasks from the store using its user-defined unique identifier. If a task with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchTask(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>)](./ockreadabletaskstore/fetchtask%28withid,callbackqueue,completion%29.md)
  `fetchTask` asynchronously retrieves an array of tasks from the store using its user-defined unique identifier. If a task with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchTasks(query: OCKTaskQuery) async throws -> [Task]](./ockreadabletaskstore/fetchtasks%28query%29.md)
  `fetchTasks` asynchronously retrieves an array of tasks from the store.
- [func fetchTasks(query: OCKTaskQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[Task]>)](./ockreadabletaskstore/fetchtasks%28query,callbackqueue,completion%29.md)
  `fetchTasks` asynchronously retrieves an array of tasks from the store.
- [func tasks(matching: OCKTaskQuery) -> Tasks](./ockreadabletaskstore/tasks%28matching%29.md)
  A continuous stream of tasks that exist in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKEventStore](./ockeventstore.md)
- [OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
- [OCKTaskStore](./ocktaskstore.md)
### Conforming Types
- [OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
- [OCKStore](./ockstore.md)

## See Also

### Care tasks
- [struct OCKTask](./ocktask.md)
  An `OCKTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.
- [protocol OCKAnyTask](./ockanytask.md)
  Conforming a type to `OCKAnyTask` allows it to be queried and displayed by CareKit.
- [protocol OCKAnyVersionableTask](./ockanyversionabletask.md)
  Any task that has a notion of versioning and is persisted in a database. Conforming a store’s task type to this protocol allows CareKit to provide default implementations for `OCKReadOnlyEventStore` methods.
- [struct OCKHealthKitTask](./ockhealthkittask.md)
  An `OCKHealthKitTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.
- [struct OCKHealthKitLinkage](./ockhealthkitlinkage.md)
  Describes how a task outcome values should be retrieved from HealthKit.
- [protocol OCKTaskStore](./ocktaskstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyTask` is considered an `OCKTaskStore`.
- [protocol OCKAnyTaskStore](./ockanytaskstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyTask` is considered an `OCKAnyTaskStore`.
- [protocol OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
  A store that allows for reading tasks.
- [struct OCKTaskQuery](./ocktaskquery.md)
  A query that limits which tasks will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadabletaskstore)*