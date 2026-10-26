---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomequery"
framework: "CareKit/CareKitStore"
---

# OCKOutcomeQuery

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

A query that limits which outcomes will be returned when fetching.

## Declaration

```swift
struct OCKOutcomeQuery
```

## Topics

### Initializers
- [init()](./ockoutcomequery/init%28%29.md)
- [init(dateInterval: DateInterval?)](./ockoutcomequery/init%28dateinterval%29.md)
- [init(for: Date)](./ockoutcomequery/init%28for%29.md)
  Create a query with that spans the entire day on the date given.
### Instance Properties
- [var dateInterval: DateInterval?](./ockoutcomequery/dateinterval.md)
- [var groupIdentifiers: [String?]](./ockoutcomequery/groupidentifiers.md)
- [var ids: [String]](./ockoutcomequery/ids.md)
- [var limit: Int?](./ockoutcomequery/limit.md)
- [var offset: Int](./ockoutcomequery/offset.md)
- [var remoteIDs: [String?]](./ockoutcomequery/remoteids.md)
- [var tags: [String]](./ockoutcomequery/tags.md)
- [var taskIDs: [String]](./ockoutcomequery/taskids.md)
  An array of task identifiers to match against.
- [var taskRemoteIDs: [String]](./ockoutcomequery/taskremoteids.md)
  An array of remote IDs of tasks for which outcomes should be returned.
- [var taskUUIDs: [UUID]](./ockoutcomequery/taskuuids.md)
  An array of universally unique identifiers of tasks for which outcomes should be returned.
- [var uuids: [UUID]](./ockoutcomequery/uuids.md)
### Default Implementations
- [Equatable Implementations](./ockoutcomequery/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

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
- [protocol OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
  A store that allows for reading outcomes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomequery)*