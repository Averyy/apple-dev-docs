---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplan"
framework: "CareKit/CareKitStore"
---

# OCKAnyCarePlan

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A protocol for a CareKit plan.

## Declaration

```swift
protocol OCKAnyCarePlan : Sendable
```

## Topics

### Instance Properties
- [var effectiveDate: Date](./ockanycareplan/effectivedate.md)
  A date specifying when this version of the care plan begins to take effect.
- [var groupIdentifier: String?](./ockanycareplan/groupidentifier.md)
  An identifier you use to group this care plan with others.
- [var id: String](./ockanycareplan/id.md)
  A user-defined unique identifier.
- [var notes: [OCKNote]?](./ockanycareplan/notes.md)
  Any array of notes associated with this object.
- [var remoteID: String?](./ockanycareplan/remoteid.md)
  An identifier for this care plan in a remote store.
- [var title: String](./ockanycareplan/title.md)
  A title describing this care plan.
### Instance Methods
- [func belongs(to: OCKAnyPatient) -> Bool](./ockanycareplan/belongs%28to%29.md)
  Determines if this care plan belongs to the given patient.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKCarePlan](./ockcareplan.md)

## See Also

### Care plans
- [struct OCKCarePlan](./ockcareplan.md)
  An `OCKCarePlan` represents a set of tasks, including both interventions and assesments, that a patient is supposed to complete as part of his or her treatment for a specific condition. For example, a care plan for obesity may include tasks requiring the patient to exercise, record their weight, and log meals. As the care plan evolves with the patient’s progress, the care provider may modify the exercises and include notes each time about why the changes were made.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplan)*