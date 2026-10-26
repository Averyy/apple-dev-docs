---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytask"
framework: "CareKit/CareKitStore"
---

# OCKAnyTask

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Conforming a type to `OCKAnyTask` allows it to be queried and displayed by CareKit.

## Declaration

```swift
protocol OCKAnyTask : Sendable
```

## Topics

### Instance Properties
- [var asset: String?](./ockanytask/asset.md)
  A string representation of an asset.
- [var effectiveDate: Date](./ockanytask/effectivedate.md)
  A date specifying when this version of the task begins taking effect.
- [var groupIdentifier: String?](./ockanytask/groupidentifier.md)
  A user-defined group identifier that can be used both for querying and sorting results. Examples may include: “medications”, “exercises”, “family”, “males”, “diabetics”, etc.
- [var id: String](./ockanytask/id.md)
  A user-defined unique identifier, typically human readable.
- [var impactsAdherence: Bool](./ockanytask/impactsadherence.md)
  If true, completion of this task will be factored into the patient’s overall adherence. True by default.
- [var instructions: String?](./ockanytask/instructions.md)
  Instructions about how this task should be performed.
- [var notes: [OCKNote]?](./ockanytask/notes.md)
  Any array of notes associated with this object.
- [var remoteID: String?](./ockanytask/remoteid.md)
  An identifier for this task in a remote store.
- [var schedule: OCKSchedule](./ockanytask/schedule.md)
  A schedule that specifies how often this task occurs.
- [var title: String?](./ockanytask/title.md)
  A title that will be used to represent this care plan to the patient.
- [var uuid: UUID](./ockanytask/uuid.md)
  An universally unique identifier for this task.
### Instance Methods
- [func belongs(to: OCKAnyCarePlan) -> Bool](./ockanytask/belongs%28to%29.md)
  Determines if this task belongs to the given care plan.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyVersionableTask](./ockanyversionabletask.md)
### Conforming Types
- [OCKHealthKitTask](./ockhealthkittask.md)
- [OCKTask](./ocktask.md)

## See Also

### Care tasks
- [struct OCKTask](./ocktask.md)
  An `OCKTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.
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
- [struct OCKTaskQuery](./ocktaskquery.md)
  A query that limits which tasks will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanytask)*