---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplan"
framework: "CareKit/CareKitStore"
---

# OCKCarePlan

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An `OCKCarePlan` represents a set of tasks, including both interventions and assesments, that a patient is supposed to complete as part of his or her treatment for a specific condition. For example, a care plan for obesity may include tasks requiring the patient to exercise, record their weight, and log meals. As the care plan evolves with the patient’s progress, the care provider may modify the exercises and include notes each time about why the changes were made.

## Declaration

```swift
struct OCKCarePlan
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockcareplan/init%28from%29.md)
- [init(id: String, title: String, patientUUID: UUID?)](./ockcareplan/init%28id,title,patientuuid%29.md)
  Initialize a care plan with a title, id, and optional patient version.
### Instance Properties
- [var asset: String?](./ockcareplan/asset.md)
- [var createdDate: Date?](./ockcareplan/createddate.md)
- [var deletedDate: Date?](./ockcareplan/deleteddate.md)
- [var effectiveDate: Date](./ockcareplan/effectivedate.md)
- [var groupIdentifier: String?](./ockcareplan/groupidentifier.md)
- [var id: String](./ockcareplan/id.md)
- [var nextVersionUUIDs: [UUID]](./ockcareplan/nextversionuuids.md)
- [var notes: [OCKNote]?](./ockcareplan/notes.md)
- [var patientUUID: UUID?](./ockcareplan/patientuuid.md)
  The UUID of the patient to whom this care plan belongs.
- [var previousVersionUUIDs: [UUID]](./ockcareplan/previousversionuuids.md)
- [var remoteID: String?](./ockcareplan/remoteid.md)
- [var schemaVersion: OCKSemanticVersion?](./ockcareplan/schemaversion.md)
- [var source: String?](./ockcareplan/source.md)
- [var tags: [String]?](./ockcareplan/tags.md)
- [var timezone: TimeZone](./ockcareplan/timezone.md)
- [var title: String](./ockcareplan/title.md)
- [var updatedDate: Date?](./ockcareplan/updateddate.md)
- [var userInfo: [String : String]?](./ockcareplan/userinfo.md)
- [var uuid: UUID](./ockcareplan/uuid.md)
### Instance Methods
- [func belongs(to: OCKAnyPatient) -> Bool](./ockcareplan/belongs%28to%29.md)
### Default Implementations
- [Equatable Implementations](./ockcareplan/equatable-implementations.md)

## Relationships

### Conforms To
- [OCKAnyCarePlan](./ockanycareplan.md)
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Care plans
- [protocol OCKAnyCarePlan](./ockanycareplan.md)
  A protocol for a CareKit plan.
- [protocol OCKCarePlanStore](./ockcareplanstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyCarePlan` is considered an `OCKCarePlanStore`.
- [protocol OCKAnyReadOnlyCarePlanStore](./ockanyreadonlycareplanstore.md)
  A store that allows for reading care plans.
- [protocol OCKReadableCarePlanStore](./ockreadablecareplanstore.md)
  A store that allows for reading care plans.
- [protocol OCKAnyCarePlanStore](./ockanycareplanstore.md)
  A protocol that enforces conformance to a care plan store.
- [struct OCKCarePlanQuery](./ockcareplanquery.md)
  A query that limits which care plans will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplan)*