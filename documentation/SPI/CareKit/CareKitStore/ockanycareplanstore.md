---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore"
framework: "CareKit/CareKitStore"
---

# OCKAnyCarePlanStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A protocol that enforces conformance to a care plan store.

## Declaration

```swift
protocol OCKAnyCarePlanStore : OCKAnyReadOnlyCarePlanStore
```

#### Overview

Any store that can write to one more types conforming to `OCKAnyCarePlan` is considered an `OCKAnyCarePlanStore`.

## Topics

### Instance Methods
- [func addAnyCarePlan(OCKAnyCarePlan) async throws -> OCKAnyCarePlan](./ockanycareplanstore/addanycareplan%28_%29.md)
  Asynchronously adds a single care plan to the store.
- [func addAnyCarePlan(OCKAnyCarePlan, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>?)](./ockanycareplanstore/addanycareplan%28_,callbackqueue,completion%29.md)
  Asynchronously adds a single care plan to the store.
- [func addAnyCarePlans([OCKAnyCarePlan]) async throws -> [OCKAnyCarePlan]](./ockanycareplanstore/addanycareplans%28_%29.md)
  Asynchronously adds an array of care plans to the store.
- [func addAnyCarePlans([OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)](./ockanycareplanstore/addanycareplans%28_,callbackqueue,completion%29.md)
  Asynchronously adds an array of care plans to the store.
- [func deleteAnyCarePlan(OCKAnyCarePlan) async throws -> OCKAnyCarePlan](./ockanycareplanstore/deleteanycareplan%28_%29.md)
  Asynchronously deletes a single care plan from the store.
- [func deleteAnyCarePlan(OCKAnyCarePlan, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>?)](./ockanycareplanstore/deleteanycareplan%28_,callbackqueue,completion%29.md)
  Asynchronously deletes a single care plan from the store.
- [func deleteAnyCarePlans([OCKAnyCarePlan]) async throws -> [OCKAnyCarePlan]](./ockanycareplanstore/deleteanycareplans%28_%29.md)
  Asynchronously deletes an array of care plans from the store.
- [func deleteAnyCarePlans([OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)](./ockanycareplanstore/deleteanycareplans%28_,callbackqueue,completion%29.md)
  Asynchronously deletes an array of care plans from the store.
- [func updateAnyCarePlan(OCKAnyCarePlan) async throws -> OCKAnyCarePlan](./ockanycareplanstore/updateanycareplan%28_%29.md)
  Asynchronously updates a single care plan in the store.
- [func updateAnyCarePlan(OCKAnyCarePlan, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>?)](./ockanycareplanstore/updateanycareplan%28_,callbackqueue,completion%29.md)
  Asynchronously updates a single care plan in the store.
- [func updateAnyCarePlans([OCKAnyCarePlan]) async throws -> [OCKAnyCarePlan]](./ockanycareplanstore/updateanycareplans%28_%29.md)
  Aynchronously updates an array of care plans in the store.
- [func updateAnyCarePlans([OCKAnyCarePlan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyCarePlan]>?)](./ockanycareplanstore/updateanycareplans%28_,callbackqueue,completion%29.md)
  Asynchronously updates an array of care plans in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyCarePlanStore](./ockanyreadonlycareplanstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKCarePlanStore](./ockcareplanstore.md)
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
- [protocol OCKAnyReadOnlyCarePlanStore](./ockanyreadonlycareplanstore.md)
  A store that allows for reading care plans.
- [protocol OCKReadableCarePlanStore](./ockreadablecareplanstore.md)
  A store that allows for reading care plans.
- [struct OCKCarePlanQuery](./ockcareplanquery.md)
  A query that limits which care plans will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore)*