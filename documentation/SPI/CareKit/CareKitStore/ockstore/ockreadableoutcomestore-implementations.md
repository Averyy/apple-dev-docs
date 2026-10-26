---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadableoutcomestore-implementations"
framework: "CareKit/CareKitStore"
---

# OCKReadableOutcomeStore Implementations

**Framework**: CareKit/CareKitStore  
**Role**: API Collection

## Topics

### Instance Methods
- [func fetchOutcome(query: OCKOutcomeQuery) async throws -> Outcome](./fetchoutcome%28query%29.md)
  `fetchOutcome` asynchronously retrieves a single outcome from the store. If more than one outcome matches the query, only the first will be returned. If no matching outcomes exist, the completion handler will be called with an error.
- [func fetchOutcome(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>)](./fetchoutcome%28query,callbackqueue,completion%29.md)
- [func fetchOutcomes(query: OCKOutcomeQuery) async throws -> [Outcome]](./fetchoutcomes%28query%29.md)
  `fetchOutcomes` asynchronously retrieves an array of outcomes from the store.
- [func fetchOutcomes(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: @Sendable (Result<[OCKOutcome], OCKStoreError>) -> Void)](./fetchoutcomes%28query,callbackqueue,completion%29.md)
- [func outcomes(matching: OCKOutcomeQuery) -> some AsyncSequence<[OCKOutcome], Error> & Sendable](./outcomes%28matching%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/ockreadableoutcomestore-implementations)*