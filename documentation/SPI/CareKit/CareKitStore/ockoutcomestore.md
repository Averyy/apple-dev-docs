---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore"
framework: "CareKit/CareKitStore"
---

# OCKOutcomeStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol OCKOutcomeStore : OCKAnyOutcomeStore, OCKReadableOutcomeStore
```

## Topics

### Instance Methods
- [func addOutcome(Outcome) async throws -> Outcome](./ockoutcomestore/addoutcome%28_%29.md)
  `addOutcome` asynchronously adds an outcome to the store.
- [func addOutcome(Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)](./ockoutcomestore/addoutcome%28_,callbackqueue,completion%29.md)
  `addOutcome` asynchronously adds an outcome to the store.
- [func addOutcomes([Outcome]) async throws -> [Outcome]](./ockoutcomestore/addoutcomes%28_%29.md)
  `addOutcomes` asynchronously adds an array of outcomes to the store.
- [func addOutcomes([Outcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Outcome]>?)](./ockoutcomestore/addoutcomes%28_,callbackqueue,completion%29.md)
  `addOutcomes` asynchronously adds an array of outcomes to the store.
- [func deleteOutcome(Outcome) async throws -> Outcome](./ockoutcomestore/deleteoutcome%28_%29.md)
  `deleteOutcome` asynchronously deletes an outcome from the store.
- [func deleteOutcome(Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)](./ockoutcomestore/deleteoutcome%28_,callbackqueue,completion%29.md)
  `deleteOutcome` asynchronously deletes an outcome from the store.
- [func deleteOutcomes([Outcome]) async throws -> [Outcome]](./ockoutcomestore/deleteoutcomes%28_%29.md)
  `deleteOutcomes` asynchronously deletes an array of outcomes from the store.
- [func deleteOutcomes([Outcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Outcome]>?)](./ockoutcomestore/deleteoutcomes%28_,callbackqueue,completion%29.md)
  `deleteOutcomes` asynchronously deletes an array of outcomes from the store.
- [func updateOutcome(Outcome) async throws -> Outcome](./ockoutcomestore/updateoutcome%28_%29.md)
  `updateOutcome` asynchronously updates an outcome in the store.
- [func updateOutcome(Outcome, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>?)](./ockoutcomestore/updateoutcome%28_,callbackqueue,completion%29.md)
  `updateOutcome` asynchronously updates an outcome in the store.
- [func updateOutcomes([Outcome]) async throws -> [Outcome]](./ockoutcomestore/updateoutcomes%28_%29.md)
  `updateOutcomes` asynchronously updates an array of outcomes in the store.
- [func updateOutcomes([Outcome], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Outcome]>?)](./ockoutcomestore/updateoutcomes%28_,callbackqueue,completion%29.md)
  `updateOutcomes` asynchronously updates an array of outcomes in the store.

## Relationships

### Inherits From
- [OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- [OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKEventStore](./ockeventstore.md)
### Conforming Types
- [OCKHealthKitPassthroughStore](./ockhealthkitpassthroughstore.md)
- [OCKStore](./ockstore.md)

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
- [protocol OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [protocol OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
  A store that allows for reading outcomes.
- [protocol OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
  A store that allows for reading outcomes.
- [struct OCKOutcomeQuery](./ockoutcomequery.md)
  A query that limits which outcomes will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomestore)*