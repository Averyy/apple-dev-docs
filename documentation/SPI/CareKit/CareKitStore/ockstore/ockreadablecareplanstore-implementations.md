---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadablecareplanstore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKReadableCarePlanStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func carePlans(matching: OCKCarePlanQuery) -> some AsyncSequence<[OCKCarePlan], Error> & Sendable](./careplans%28matching%29.md)
- [func fetchCarePlan(withID: String) async throws -> Plan](./fetchcareplan%28withid%29.md)
  `fetchCarePlan` asynchronously retrieves a care plan from the store using its user-defined unique identifier. If a care plan with the specified identifier is not found, the completion handler will be called with an error.
- [func fetchCarePlan(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Plan>)](./fetchcareplan%28withid,callbackqueue,completion%29.md)
- [func fetchCarePlans(query: OCKCarePlanQuery) async throws -> [Plan]](./fetchcareplans%28query%29.md)
  `fetchCarePlans` asynchronously retrieves an array of care plans from the store.
- [func fetchCarePlans(query: OCKCarePlanQuery, callbackQueue: DispatchQueue, completion: @Sendable (Result<[OCKCarePlan], OCKStoreError>) -> Void)](./fetchcareplans%28query,callbackqueue,completion%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadablecareplanstore-implementations)*