---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyReadOnlyCarePlanStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading care plans.

## Declaration

```swift
protocol OCKAnyReadOnlyCarePlanStore : OCKAnyResettableStore
```

## Topics

### Instance Methods
- [func anyCarePlans(matching: OCKCarePlanQuery) -> CareStoreQueryResults<OCKAnyCarePlan>](./ockanyreadonlycareplanstore/anycareplans%28matching%29.md)
  A continuous stream of care plans that exist in the store.
- [func fetchAnyCarePlan(withID: String) async throws -> OCKAnyCarePlan](./ockanyreadonlycareplanstore/fetchanycareplan%28withid%29.md)
  Asynchronously retrieves a single care plans from the store.
- [func fetchAnyCarePlan(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>)](./ockanyreadonlycareplanstore/fetchanycareplan%28withid,callbackqueue,completion%29.md)
  Asynchronously retrieves a single care plan from the store.
- [func fetchAnyCarePlans(query: OCKCarePlanQuery) async throws -> [OCKAnyCarePlan]](./ockanyreadonlycareplanstore/fetchanycareplans%28query%29.md)
  Aynchronously retrieves an array of care plans from the store.
- [func fetchAnyCarePlans(query: OCKCarePlanQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>)](./ockanyreadonlycareplanstore/fetchanycareplans%28query,callbackqueue,completion%29.md)
  A continuous stream of care plans that exist in the store. The stream yields a new value whenever the result changes and yields an error if there’s an issue accessing the store or fetching results.

## Relationships

### Inherits From
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyCarePlanStore](./ockanycareplanstore.md)
- [OCKCarePlanStore](./ockcareplanstore.md)
- [OCKReadableCarePlanStore](./ockreadablecareplanstore.md)
### Conforming Types
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

## See Also

### Care plans
- [struct OCKCarePlan](./ockcareplan.md)
  An `OCKCarePlan` represents a set of tasks, including both interventions and assesments, that a patient is supposed to complete as part of his or her treatment for a specific condition. For example, a care plan for obesity may include tasks requiring the patient to exercise, record their weight, and log meals. As the care plan evolves with the patient’s progress, the care provider may modify the exercises and include notes each time about why the changes were made.
- [protocol OCKAnyCarePlan](./ockanycareplan.md)
  A protocol for a CareKit plan.
- [protocol OCKCarePlanStore](./ockcareplanstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyCarePlan` is considered an `OCKCarePlanStore`.
- [protocol OCKReadableCarePlanStore](./ockreadablecareplanstore.md)
  A store that allows for reading care plans.
- [protocol OCKAnyCarePlanStore](./ockanycareplanstore.md)
  A protocol that enforces conformance to a care plan store.
- [struct OCKCarePlanQuery](./ockcareplanquery.md)
  A query that limits which care plans will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycareplanstore)*