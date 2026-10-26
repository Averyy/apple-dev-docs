---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyversionabletask"
framework: "CareKit/CareKitStore"
---

# OCKAnyVersionableTask

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any task that has a notion of versioning and is persisted in a database. Conforming a store’s task type to this protocol allows CareKit to provide default implementations for `OCKReadOnlyEventStore` methods.

## Declaration

```swift
protocol OCKAnyVersionableTask : OCKAnyTask
```

## Topics

### Instance Properties
- [var effectiveDate: Date](./ockanyversionabletask/effectivedate.md)
  A date specifying when this version of the task begins taking effect.
- [var nextVersionUUIDs: [UUID]](./ockanyversionabletask/nextversionuuids.md)
  An identifier that uniquely identifies the next version of the task in a database.
- [var previousVersionUUIDs: [UUID]](./ockanyversionabletask/previousversionuuids.md)
  An identifier that uniquely identifies the previous version of the task in a database.

## Relationships

### Inherits From
- [OCKAnyTask](./ockanytask.md)
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKHealthKitTask](./ockhealthkittask.md)
- [OCKTask](./ocktask.md)

## See Also

### Care tasks
- [struct OCKTask](./ocktask.md)
  An `OCKTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.
- [protocol OCKAnyTask](./ockanytask.md)
  Conforming a type to `OCKAnyTask` allows it to be queried and displayed by CareKit.
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
- [struct OCKTaskQuery](./ocktaskquery.md)
  A query that limits which tasks will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyversionabletask)*