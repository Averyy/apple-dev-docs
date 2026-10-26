---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyTaskStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store able to write to one ore more types conforming to `OCKAnyTask` is considered an `OCKAnyTaskStore`.

## Declaration

```swift
protocol OCKAnyTaskStore : OCKAnyReadOnlyTaskStore
```

## Topics

### Instance Methods
- [func addAnyTask(OCKAnyTask) async throws -> OCKAnyTask](./ockanytaskstore/addanytask%28_%29.md)
  Asynchronously add a task to the store.
- [func addAnyTask(OCKAnyTask, callbackQueue: DispatchQueue, completion: (@Sendable (Result<OCKAnyTask, OCKStoreError>) -> Void)?)](./ockanytaskstore/addanytask%28_,callbackqueue,completion%29.md)
  Asynchronously add a task to the store.
- [func addAnyTasks([OCKAnyTask]) async throws -> [OCKAnyTask]](./ockanytaskstore/addanytasks%28_%29.md)
  Asynchronously add an array of tasks to the store.
- [func addAnyTasks([OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)](./ockanytaskstore/addanytasks%28_,callbackqueue,completion%29.md)
  Asynchronously add an array of tasks to the store.
- [func deleteAnyTask(OCKAnyTask) async throws -> OCKAnyTask](./ockanytaskstore/deleteanytask%28_%29.md)
  Asynchronously delete a task from the store.
- [func deleteAnyTask(OCKAnyTask, callbackQueue: DispatchQueue, completion: (@Sendable (Result<OCKAnyTask, OCKStoreError>) -> Void)?)](./ockanytaskstore/deleteanytask%28_,callbackqueue,completion%29.md)
  Asynchronously delete a task from the store.
- [func deleteAnyTasks([OCKAnyTask]) async throws -> [OCKAnyTask]](./ockanytaskstore/deleteanytasks%28_%29.md)
  Asynchronously delete an array of tasks from the store.
- [func deleteAnyTasks([OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)](./ockanytaskstore/deleteanytasks%28_,callbackqueue,completion%29.md)
  Asynchronously delete an array of tasks from the store.
- [func updateAnyTask(OCKAnyTask) async throws -> OCKAnyTask](./ockanytaskstore/updateanytask%28_%29.md)
  Asynchronously update a task in the store.
- [func updateAnyTask(OCKAnyTask, callbackQueue: DispatchQueue, completion: (@Sendable (Result<OCKAnyTask, OCKStoreError>) -> Void)?)](./ockanytaskstore/updateanytask%28_,callbackqueue,completion%29.md)
  Asynchronously update a task in the store.
- [func updateAnyTasks([OCKAnyTask]) async throws -> [OCKAnyTask]](./ockanytaskstore/updateanytasks%28_%29.md)
  Asynchronously update an array of tasks in the store.
- [func updateAnyTasks([OCKAnyTask], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyTask]>?)](./ockanytaskstore/updateanytasks%28_,callbackqueue,completion%29.md)
  Asynchronously update an array of tasks in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyEventStore](./ockanyeventstore.md)
- [OCKEventStore](./ockeventstore.md)
- [OCKTaskStore](./ocktaskstore.md)
### Conforming Types
- [OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

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
- [protocol OCKReadableTaskStore](./ockreadabletaskstore.md)
  A store that allows for reading tasks.
- [protocol OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
  A store that allows for reading tasks.
- [struct OCKTaskQuery](./ocktaskquery.md)
  A query that limits which tasks will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytaskstore)*