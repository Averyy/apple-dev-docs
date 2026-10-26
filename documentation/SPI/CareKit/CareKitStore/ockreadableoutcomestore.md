---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore"
framework: "CareKit/CareKitStore"
---

# OCKReadableOutcomeStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading outcomes.

## Declaration

```swift
protocol OCKReadableOutcomeStore : OCKAnyReadOnlyOutcomeStore
```

## Topics

### Associated Types
- [associatedtype Outcome : OCKAnyOutcome, Equatable, Identifiable](./ockreadableoutcomestore/outcome.md)
- [associatedtype Outcomes : Sendable, AsyncSequence](./ockreadableoutcomestore/outcomes.md)
  An asynchronous sequence that produces outcomes.
### Instance Methods
- [func fetchOutcome(query: OCKOutcomeQuery) async throws -> Outcome](./ockreadableoutcomestore/fetchoutcome%28query%29.md)
  `fetchOutcome` asynchronously retrieves a single outcome from the store. If more than one outcome matches the query, only the first will be returned. If no matching outcomes exist, the completion handler will be called with an error.
- [func fetchOutcome(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<Outcome>)](./ockreadableoutcomestore/fetchoutcome%28query,callbackqueue,completion%29.md)
  Fetch a list of events that exist in the store.
- [func fetchOutcomes(query: OCKOutcomeQuery) async throws -> [Outcome]](./ockreadableoutcomestore/fetchoutcomes%28query%29.md)
  `fetchOutcomes` asynchronously retrieves an array of outcomes from the store.
- [func fetchOutcomes(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[Outcome]>)](./ockreadableoutcomestore/fetchoutcomes%28query,callbackqueue,completion%29.md)
  Fetch a list of events that exist in the store.
- [func outcomes(matching: OCKOutcomeQuery) -> Outcomes](./ockreadableoutcomestore/outcomes%28matching%29.md)
  A continuous stream of outcomes that exist in the store.

## Relationships

### Inherits From
- [OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKEventStore](./ockeventstore.md)
- [OCKOutcomeStore](./ockoutcomestore.md)
- [OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
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
- [protocol OCKOutcomeStore](./ockoutcomestore.md)
- [protocol OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [protocol OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
  A store that allows for reading outcomes.
- [struct OCKOutcomeQuery](./ockoutcomequery.md)
  A query that limits which outcomes will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadableoutcomestore)*