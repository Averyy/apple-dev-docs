---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore"
framework: "CareKit/CareKitStore"
---

# OCKAnyReadOnlyOutcomeStore

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A store that allows for reading outcomes.

## Declaration

```swift
protocol OCKAnyReadOnlyOutcomeStore : OCKAnyResettableStore
```

## Topics

### Instance Methods
- [func anyOutcomes(matching: OCKOutcomeQuery) -> CareStoreQueryResults<OCKAnyOutcome>](./ockanyreadonlyoutcomestore/anyoutcomes%28matching%29.md)
  A continuous stream of outcomes that exist in the store.
- [func fetchAnyOutcome(query: OCKOutcomeQuery) async throws -> OCKAnyOutcome](./ockanyreadonlyoutcomestore/fetchanyoutcome%28query%29.md)
  Asynchronously retrieve a single outcome from the store.
- [func fetchAnyOutcome(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyOutcome>)](./ockanyreadonlyoutcomestore/fetchanyoutcome%28query,callbackqueue,completion%29.md)
  Fetch an outcome from the store.
- [func fetchAnyOutcomes(query: OCKOutcomeQuery) async throws -> [OCKAnyOutcome]](./ockanyreadonlyoutcomestore/fetchanyoutcomes%28query%29.md)
  Asynchronously retrieve an array of outcomes from the store.
- [func fetchAnyOutcomes(query: OCKOutcomeQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyOutcome]>)](./ockanyreadonlyoutcomestore/fetchanyoutcomes%28query,callbackqueue,completion%29.md)
  Fetch a list of outcomes that exist in the store.

## Relationships

### Inherits From
- [OCKAnyResettableStore](./ockanyresettablestore.md)
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [OCKAnyEventStore](./ockanyeventstore.md)
- [OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [OCKAnyReadOnlyEventStore](./ockanyreadonlyeventstore.md)
- [OCKEventStore](./ockeventstore.md)
- [OCKOutcomeStore](./ockoutcomestore.md)
- [OCKReadOnlyEventStore](./ockreadonlyeventstore.md)
- [OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
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
- [protocol OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [protocol OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
  A store that allows for reading outcomes.
- [struct OCKOutcomeQuery](./ockoutcomequery.md)
  A query that limits which outcomes will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlyoutcomestore)*