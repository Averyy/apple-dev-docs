---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore"
framework: "CareKit/CareKitStore"
---

# OCKCarePlanStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

Any store that can perform read and write operations on a single type conforming to `OCKAnyCarePlan` is considered an `OCKCarePlanStore`.

## Declaration

```swift
protocol OCKCarePlanStore : OCKAnyCarePlanStore, OCKReadableCarePlanStore
```

## Topics

### Instance Methods
- [func addCarePlan(Plan) async throws -> Plan](./ockcareplanstore/addcareplan%28_%29.md)
  `addCarePlan` asynchronously adds a care plans to the store.
- [func addCarePlan(Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)](./ockcareplanstore/addcareplan%28_,callbackqueue,completion%29.md)
  `addCarePlan` asynchronously adds a care plans to the store.
- [func addCarePlans([Plan]) async throws -> [Plan]](./ockcareplanstore/addcareplans%28_%29.md)
  `addCarePlans` asynchronously adds an array of care plans to the store.
- [func addCarePlans([Plan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Plan]>?)](./ockcareplanstore/addcareplans%28_,callbackqueue,completion%29.md)
  `addCarePlans` asynchronously adds an array of care plans to the store.
- [func deleteCarePlan(Plan) async throws -> Plan](./ockcareplanstore/deletecareplan%28_%29.md)
  `deleteCarePlan` asynchronously deletes a care plan from the store.
- [func deleteCarePlan(Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)](./ockcareplanstore/deletecareplan%28_,callbackqueue,completion%29.md)
  `deleteCarePlan` asynchronously deletes a care plan from the store.
- [func deleteCarePlans([Plan]) async throws -> [Plan]](./ockcareplanstore/deletecareplans%28_%29.md)
  `deleteCarePlans` asynchronously deletes an array of care plans from the store.
- [func deleteCarePlans([Plan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Plan]>?)](./ockcareplanstore/deletecareplans%28_,callbackqueue,completion%29.md)
  `deleteCarePlans` asynchronously deletes an array of care plans from the store.
- [func updateCarePlan(Plan) async throws -> Plan](./ockcareplanstore/updatecareplan%28_%29.md)
  `updateCarePlan` asynchronously updates a care plan in the store.
- [func updateCarePlan(Plan, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>?)](./ockcareplanstore/updatecareplan%28_,callbackqueue,completion%29.md)
  `updateCarePlan` asynchronously updates a care plan in the store.
- [func updateCarePlans([Plan]) async throws -> [Plan]](./ockcareplanstore/updatecareplans%28_%29.md)
  `updateCarePlans` asynchronously updates an array of care plans in the store.
- [func updateCarePlans([Plan], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Plan]>?)](./ockcareplanstore/updatecareplans%28_,callbackqueue,completion%29.md)
  `updateCarePlans` asynchronously updates an array of care plans in the store.

## Relationships

### Inherits From
- [OCKAnyCarePlanStore](./ockanycareplanstore.md)
- [OCKAnyReadOnlyCarePlanStore](./ockanyreadonlycareplanstore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKReadableCarePlanStore](./ockreadablecareplanstore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKStore](./ockstore.md)

## See Also

### Care plans
- [struct OCKCarePlan](./ockcareplan.md)
  An `OCKCarePlan` represents a set of tasks, including both interventions and assesments, that a patient is supposed to complete as part of his or her treatment for a specific condition. For example, a care plan for obesity may include tasks requiring the patient to exercise, record their weight, and log meals. As the care plan evolves with the patient’s progress, the care provider may modify the exercises and include notes each time about why the changes were made.
- [protocol OCKAnyCarePlan](./ockanycareplan.md)
  A protocol for a CareKit plan.
- [protocol OCKAnyReadOnlyCarePlanStore](./ockanyreadonlycareplanstore.md)
  A store that allows for reading care plans.
- [protocol OCKReadableCarePlanStore](./ockreadablecareplanstore.md)
  A store that allows for reading care plans.
- [protocol OCKAnyCarePlanStore](./ockanycareplanstore.md)
  A protocol that enforces conformance to a care plan store.
- [struct OCKCarePlanQuery](./ockcareplanquery.md)
  A query that limits which care plans will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcareplanstore)*