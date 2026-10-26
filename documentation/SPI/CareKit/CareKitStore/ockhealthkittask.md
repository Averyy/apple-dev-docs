---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkittask"
framework: "CareKit/CareKitStore"
---

# OCKHealthKitTask

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An `OCKHealthKitTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.

## Declaration

```swift
struct OCKHealthKitTask
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockhealthkittask/init%28from%29.md)
- [init(id: String, title: String?, carePlanUUID: UUID?, schedule: OCKSchedule, healthKitLinkage: OCKHealthKitLinkage)](./ockhealthkittask/init%28id,title,careplanuuid,schedule,healthkitlinkage%29.md)
  Instantiate a new `OCKHealthKitTask`
### Instance Properties
- [var asset: String?](./ockhealthkittask/asset.md)
- [var carePlanUUID: UUID?](./ockhealthkittask/careplanuuid.md)
  The UUID of the care plan to which this task belongs.
- [var createdDate: Date?](./ockhealthkittask/createddate.md)
- [var deletedDate: Date?](./ockhealthkittask/deleteddate.md)
- [var effectiveDate: Date](./ockhealthkittask/effectivedate.md)
- [var groupIdentifier: String?](./ockhealthkittask/groupidentifier.md)
- [var healthKitLinkage: OCKHealthKitLinkage](./ockhealthkittask/healthkitlinkage.md)
  A structure specifying how this task is linked with HealthKit.
- [var id: String](./ockhealthkittask/id.md)
- [var impactsAdherence: Bool](./ockhealthkittask/impactsadherence.md)
- [var instructions: String?](./ockhealthkittask/instructions.md)
- [var nextVersionUUIDs: [UUID]](./ockhealthkittask/nextversionuuids.md)
- [var notes: [OCKNote]?](./ockhealthkittask/notes.md)
- [var previousVersionUUIDs: [UUID]](./ockhealthkittask/previousversionuuids.md)
- [var remoteID: String?](./ockhealthkittask/remoteid.md)
- [var schedule: OCKSchedule](./ockhealthkittask/schedule.md)
- [var schemaVersion: OCKSemanticVersion?](./ockhealthkittask/schemaversion.md)
- [var source: String?](./ockhealthkittask/source.md)
- [var tags: [String]?](./ockhealthkittask/tags.md)
- [var timezone: TimeZone](./ockhealthkittask/timezone.md)
- [var title: String?](./ockhealthkittask/title.md)
- [var updatedDate: Date?](./ockhealthkittask/updateddate.md)
- [var userInfo: [String : String]?](./ockhealthkittask/userinfo.md)
- [var uuid: UUID](./ockhealthkittask/uuid.md)
### Instance Methods
- [func belongs(to: OCKAnyCarePlan) -> Bool](./ockhealthkittask/belongs%28to%29.md)
### Default Implementations
- [Equatable Implementations](./ockhealthkittask/equatable-implementations.md)

## Relationships

### Conforms To
- [OCKAnyTask](./ockanytask.md)
- [OCKAnyVersionableTask](./ockanyversionabletask.md)
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkittask)*