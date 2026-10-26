---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore"
framework: "CareKit/CareKitStore"
---

# OCKReadableCarePlanStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading care plans.

## Declaration

```swift
protocol OCKReadableCarePlanStore : OCKAnyReadOnlyCarePlanStore
```

## Topics

### Associated Types
- [associatedtype Plan : OCKAnyCarePlan, Equatable, Identifiable](./ockreadablecareplanstore/plan.md)
- [associatedtype Plans : Sendable, AsyncSequence](./ockreadablecareplanstore/plans.md)
  An asynchronous sequence that produces care plans.
### Instance Methods
- [func carePlans(matching: OCKCarePlanQuery) -> Plans](./ockreadablecareplanstore/careplans%28matching%29.md)
  A continuous stream of care plans that exist in the store.
- [func fetchCarePlan(withID: String) async throws -> Plan](./ockreadablecareplanstore/fetchcareplan%28withid%29.md)
  `fetchCarePlan` asynchronously retrieves a care plan from the store using its user-defined unique identifier. If a care plan with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchCarePlan(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>)](./ockreadablecareplanstore/fetchcareplan%28withid,callbackqueue,completion%29.md)
  `fetchCarePlan` asynchronously retrieves a care plan from the store using its user-defined unique identifier. If a care plan with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchCarePlans(query: OCKCarePlanQuery) async throws -> [Plan]](./ockreadablecareplanstore/fetchcareplans%28query%29.md)
  `fetchCarePlans` asynchronously retrieves an array of care plans from the store.
- [func fetchCarePlans(query: OCKCarePlanQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[Plan]>)](./ockreadablecareplanstore/fetchcareplans%28query,callbackqueue,completion%29.md)
  `fetchCarePlans` asynchronously retrieves an array of care plans from the store.

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
- [protocol OCKAnyCarePlanStore](./ockanycareplanstore.md)
  A protocol that enforces conformance to a care plan store.
- [struct OCKCarePlanQuery](./ockcareplanquery.md)
  A query that limits which care plans will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore)*