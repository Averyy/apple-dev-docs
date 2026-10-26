---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore"
framework: "CareKit/CareKitStore"
---

# OCKTaskStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store that can perform read and write operations on a single type conforming to `OCKAnyTask` is considered an `OCKTaskStore`.

## Declaration

```swift
protocol OCKTaskStore : OCKAnyTaskStore, OCKReadableTaskStore
```

## Topics

### Instance Methods
- [func addTask(Task) async throws -> Task](./ocktaskstore/addtask%28_%29.md)
  `addTask` asynchronously adds a task to the store.
- [func addTask(Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)](./ocktaskstore/addtask%28_,callbackqueue,completion%29.md)
  `addTask` asynchronously adds a task to the store.
- [func addTasks([Task]) async throws -> [Task]](./ocktaskstore/addtasks%28_%29.md)
  `addTasks` asynchronously adds an array of tasks to the store.
- [func addTasks([Task], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Task]>?)](./ocktaskstore/addtasks%28_,callbackqueue,completion%29.md)
  `addTasks` asynchronously adds an array of tasks to the store.
- [func deleteTask(Task) async throws -> Task](./ocktaskstore/deletetask%28_%29.md)
  `deleteTask` asynchronously deletes a task from the store.
- [func deleteTask(Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)](./ocktaskstore/deletetask%28_,callbackqueue,completion%29.md)
  `deleteTask` asynchronously deletes a task from the store.
- [func deleteTasks([Task]) async throws -> [Task]](./ocktaskstore/deletetasks%28_%29.md)
  `deleteTasks` asynchronously deletes an array of tasks from the store.
- [func deleteTasks([Task], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Task]>?)](./ocktaskstore/deletetasks%28_,callbackqueue,completion%29.md)
  `deleteTasks` asynchronously deletes an array of tasks from the store.
- [func updateTask(Task) async throws -> Task](./ocktaskstore/updatetask%28_%29.md)
  `updateTask` asynchronously updates a task in the store.
- [func updateTask(Task, callbackQueue: DispatchQueue, completion: OCKResultClosure<Task>?)](./ocktaskstore/updatetask%28_,callbackqueue,completion%29.md)
  `updateTask` asynchronously updates a task in the store.
- [func updateTasks([Task]) async throws -> [Task]](./ocktaskstore/updatetasks%28_%29.md)
  `updateTasks` asynchronously updates an array of tasks in the store.
- [func updateTasks([Task], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Task]>?)](./ocktaskstore/updatetasks%28_,callbackqueue,completion%29.md)
  `updateTasks` asynchronously updates an array of tasks in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKAnyTaskStore](./ockanytaskstore.md)
- [OCKReadableTaskStore](./ockreadabletaskstore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKEventStore](./ockeventstore.md)
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
- [protocol OCKAnyTaskStore](./ockanytaskstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyTask` is considered an `OCKAnyTaskStore`.
- [protocol OCKReadableTaskStore](./ockreadabletaskstore.md)
  A store that allows for reading tasks.
- [protocol OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
  A store that allows for reading tasks.
- [struct OCKTaskQuery](./ocktaskquery.md)
  A query that limits which tasks will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskstore)*