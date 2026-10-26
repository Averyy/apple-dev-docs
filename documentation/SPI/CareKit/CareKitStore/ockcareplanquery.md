---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanquery"
framework: "CareKit/CareKitStore"
---

# OCKCarePlanQuery

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A query that limits which care plans will be returned when fetching.

## Declaration

```swift
struct OCKCarePlanQuery
```

## Topics

### Initializers
- [init()](./ockcareplanquery/init%28%29.md)
- [init(dateInterval: DateInterval?)](./ockcareplanquery/init%28dateinterval%29.md)
- [init(for: Date)](./ockcareplanquery/init%28for%29.md)
  Create a query with that spans the entire day on the date given.
- [init(id: String)](./ockcareplanquery/init%28id%29.md)
### Instance Properties
- [var dateInterval: DateInterval?](./ockcareplanquery/dateinterval.md)
- [var groupIdentifiers: [String?]](./ockcareplanquery/groupidentifiers.md)
- [var ids: [String]](./ockcareplanquery/ids.md)
- [var limit: Int?](./ockcareplanquery/limit.md)
- [var offset: Int](./ockcareplanquery/offset.md)
- [var patientIDs: [String]](./ockcareplanquery/patientids.md)
  An array of patient identifiers to match against.
- [var patientRemoteIDs: [String]](./ockcareplanquery/patientremoteids.md)
  The remote ID of patients for which care plans should match.
- [var patientUUIDs: [UUID]](./ockcareplanquery/patientuuids.md)
  The UUID the patients for which care plans should match.
- [var remoteIDs: [String?]](./ockcareplanquery/remoteids.md)
- [var sortDescriptors: [SortDescriptor]](./ockcareplanquery/sortdescriptors.md)
  The order in which the results will be sorted when returned from the query.
- [var tags: [String]](./ockcareplanquery/tags.md)
- [var uuids: [UUID]](./ockcareplanquery/uuids.md)
### Enumerations
- [OCKCarePlanQuery.SortDescriptor](./ockcareplanquery/sortdescriptor.md)
  Specifies the order in which query results will be sorted.
### Default Implementations
- [Equatable Implementations](./ockcareplanquery/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Care plans
- [struct OCKCarePlan](./ockcareplan.md)
  An `OCKCarePlan` represents a set of tasks, including both interventions and assesments, that a patient is supposed to complete as part of his or her treatment for a specific condition. For example, a care plan for obesity may include tasks requiring the patient to exercise, record their weight, and log meals. As the care plan evolves with the patient’s progress, the care provider may modify the exercises and include notes each time about why the changes were made.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanquery)*