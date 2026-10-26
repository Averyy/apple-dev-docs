---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktask"
framework: "CareKit/CareKitStore"
---

# OCKTask

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An `OCKTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.

## Declaration

```swift
struct OCKTask
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ocktask/init%28from%29.md)
- [init(id: String, title: String?, carePlanUUID: UUID?, schedule: OCKSchedule)](./ocktask/init%28id,title,careplanuuid,schedule%29.md)
  Instantiate a new `OCKTask`
### Instance Properties
- [var asset: String?](./ocktask/asset.md)
- [var carePlanUUID: UUID?](./ocktask/careplanuuid.md)
  The UUID of the care plan to which this task belongs.
- [var createdDate: Date?](./ocktask/createddate.md)
- [var deletedDate: Date?](./ocktask/deleteddate.md)
- [var effectiveDate: Date](./ocktask/effectivedate.md)
- [var groupIdentifier: String?](./ocktask/groupidentifier.md)
- [var id: String](./ocktask/id.md)
- [var impactsAdherence: Bool](./ocktask/impactsadherence.md)
- [var instructions: String?](./ocktask/instructions.md)
- [var nextVersionUUIDs: [UUID]](./ocktask/nextversionuuids.md)
- [var notes: [OCKNote]?](./ocktask/notes.md)
- [var previousVersionUUIDs: [UUID]](./ocktask/previousversionuuids.md)
- [var remoteID: String?](./ocktask/remoteid.md)
- [var schedule: OCKSchedule](./ocktask/schedule.md)
- [var schemaVersion: OCKSemanticVersion?](./ocktask/schemaversion.md)
- [var source: String?](./ocktask/source.md)
- [var tags: [String]?](./ocktask/tags.md)
- [var timezone: TimeZone](./ocktask/timezone.md)
- [var title: String?](./ocktask/title.md)
- [var updatedDate: Date?](./ocktask/updateddate.md)
- [var userInfo: [String : String]?](./ocktask/userinfo.md)
- [var uuid: UUID](./ocktask/uuid.md)
### Instance Methods
- [func belongs(to: OCKAnyCarePlan) -> Bool](./ocktask/belongs%28to%29.md)
### Default Implementations
- [Equatable Implementations](./ocktask/equatable-implementations.md)

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
- [struct OCKTaskQuery](./ocktaskquery.md)
  A query that limits which tasks will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ocktask)*