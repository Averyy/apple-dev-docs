---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore"
framework: "CareKit/CareKitStore"
---

# OCKAnyOutcomeStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol OCKAnyOutcomeStore : OCKAnyReadOnlyOutcomeStore
```

## Topics

### Instance Methods
- [func addAnyOutcome(OCKAnyOutcome) async throws -> OCKAnyOutcome](./ockanyoutcomestore/addanyoutcome%28_%29.md)
  Asynchronously add an outcome to the store.
- [func addAnyOutcome(OCKAnyOutcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>?)](./ockanyoutcomestore/addanyoutcome%28_,callbackqueue,completion%29.md)
  Asynchronously add an outcome to the store.
- [func addAnyOutcomes([OCKAnyOutcome]) async throws -> [OCKAnyOutcome]](./ockanyoutcomestore/addanyoutcomes%28_%29.md)
  Asynchronously add an array of outcomes to the store.
- [func addAnyOutcomes([OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)](./ockanyoutcomestore/addanyoutcomes%28_,callbackqueue,completion%29.md)
  Asynchronously add an array of outcomes to the store.
- [func deleteAnyOutcome(OCKAnyOutcome) async throws -> OCKAnyOutcome](./ockanyoutcomestore/deleteanyoutcome%28_%29.md)
  Asynchronously delete an outcome from the store.
- [func deleteAnyOutcome(OCKAnyOutcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>?)](./ockanyoutcomestore/deleteanyoutcome%28_,callbackqueue,completion%29.md)
  Asynchronously delete an outcome from the store.
- [func deleteAnyOutcomes([OCKAnyOutcome]) async throws -> [OCKAnyOutcome]](./ockanyoutcomestore/deleteanyoutcomes%28_%29.md)
  Asynchronously delete an array of outcomes from the store.
- [func deleteAnyOutcomes([OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)](./ockanyoutcomestore/deleteanyoutcomes%28_,callbackqueue,completion%29.md)
  Asynchronously delete an array of outcomes from the store.
- [func updateAnyOutcome(OCKAnyOutcome) async throws -> OCKAnyOutcome](./ockanyoutcomestore/updateanyoutcome%28_%29.md)
  Asynchronously update an outcome in the store.
- [func updateAnyOutcome(OCKAnyOutcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>?)](./ockanyoutcomestore/updateanyoutcome%28_,callbackqueue,completion%29.md)
  Asynchronously update an outcome in the store.
- [func updateAnyOutcomes([OCKAnyOutcome]) async throws -> [OCKAnyOutcome]](./ockanyoutcomestore/updateanyoutcomes%28_%29.md)
  Asynchronously update an array of outcomes in the store.
- [func updateAnyOutcomes([OCKAnyOutcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>?)](./ockanyoutcomestore/updateanyoutcomes%28_,callbackqueue,completion%29.md)
  Asynchronously update an array of outcomes in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyEventStore](./ockanyeventstore.md)
- [OCKEventStore](./ockeventstore.md)
- [OCKOutcomeStore](./ockoutcomestore.md)
### Conforming Types
- [OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
- [OCKStore](./ockstore.md)
- [OCKStoreCoordinator](./ockstorecoordinator.md)

## See Also

### Outcomes
- [struct OCKOutcome](./ockoutcome.md)
  An `OCKOutcome` represents the outcome of an event corresponding to a task. An outcome may have 0 or more values associated with it. For example, a task that asks a patient to measure their temperature will have events whose outcome will contain a single value representing the patient’s temperature.
- [protocol OCKAnyOutcome](./ockanyoutcome.md)
  A protocol that allows CareKit to query and display outcomes.
- [struct OCKOutcomeValue](./ockoutcomevalue.md)
  An `OCKOutcomeValue` is a representation of any response of measurement that a user gives in response to a task. The underlying type could be any of a number of types including integers, booleans, dates, text, and binary data, among others.
- [enum OCKOutcomeValueType](./ockoutcomevaluetype.md)
  An enumerator specifying the types of values that can be saved to an `OCKStore`.
- [protocol OCKOutcomeValueUnderlyingType](./ockoutcomevalueunderlyingtype.md)
  Any value that can be persisted to `OCKStore` must conform to this protocol.
- [struct OCKHealthKitOutcome](./ockhealthkitoutcome.md)
- [protocol OCKOutcomeStore](./ockoutcomestore.md)
- [protocol OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
  A store that allows for reading outcomes.
- [protocol OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
  A store that allows for reading outcomes.
- [struct OCKOutcomeQuery](./ockoutcomequery.md)
  A query that limits which outcomes will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcomestore)*