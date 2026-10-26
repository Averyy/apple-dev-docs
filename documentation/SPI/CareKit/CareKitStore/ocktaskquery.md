---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskquery"
framework: "CareKit/CareKitStore"
---

# OCKTaskQuery

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A query that limits which tasks will be returned when fetching.

## Declaration

```swift
struct OCKTaskQuery
```

## Topics

### Initializers
- [init()](./ocktaskquery/init%28%29.md)
- [init(dateInterval: DateInterval?)](./ocktaskquery/init%28dateinterval%29.md)
- [init(for: Date)](./ocktaskquery/init%28for%29.md)
  Create a query with that spans the entire day on the date given.
- [init(id: String)](./ocktaskquery/init%28id%29.md)
### Instance Properties
- [var carePlanIDs: [String]](./ocktaskquery/careplanids.md)
  An array of care plan identifiers to match against.
- [var carePlanRemoteIDs: [String]](./ocktaskquery/careplanremoteids.md)
  The remote IDs of the care plans for which tasks should match.
- [var carePlanUUIDs: [UUID]](./ocktaskquery/careplanuuids.md)
  The version of the care plans for which tasks should match.
- [var dateInterval: DateInterval?](./ocktaskquery/dateinterval.md)
- [var excludesTasksWithNoEvents: Bool](./ocktaskquery/excludestaskswithnoevents.md)
  Determines if tasks with no events should be included in the query results or not. False be default.
- [var groupIdentifiers: [String?]](./ocktaskquery/groupidentifiers.md)
- [var ids: [String]](./ocktaskquery/ids.md)
- [var limit: Int?](./ocktaskquery/limit.md)
- [var offset: Int](./ocktaskquery/offset.md)
- [var remoteIDs: [String?]](./ocktaskquery/remoteids.md)
- [var sortDescriptors: [SortDescriptor]](./ocktaskquery/sortdescriptors.md)
  The order in which the results will be sorted when returned from the query.
- [var tags: [String]](./ocktaskquery/tags.md)
- [var uuids: [UUID]](./ocktaskquery/uuids.md)
### Enumerations
- [OCKTaskQuery.SortDescriptor](./ocktaskquery/sortdescriptor.md)
  Specifies the order in which query results will be sorted.
### Default Implementations
- [Equatable Implementations](./ocktaskquery/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

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
- [protocol OCKReadableTaskStore](./ockreadabletaskstore.md)
  A store that allows for reading tasks.
- [protocol OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
  A store that allows for reading tasks.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktaskquery)*