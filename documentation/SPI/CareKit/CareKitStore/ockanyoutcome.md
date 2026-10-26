---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcome"
framework: "CareKit/CareKitStore"
---

# OCKAnyOutcome

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

A protocol that allows CareKit to query and display outcomes.

## Declaration

```swift
protocol OCKAnyOutcome : Sendable
```

## Topics

### Instance Properties
- [var groupIdentifier: String?](./ockanyoutcome/groupidentifier.md)
  An identifier you can use to group this outcome with others.
- [var id: String](./ockanyoutcome/id.md)
  A human readable, user-defined unique identifier.
- [var notes: [OCKNote]?](./ockanyoutcome/notes.md)
  Any array of notes associated with this object.
- [var remoteID: String?](./ockanyoutcome/remoteid.md)
  An identifier for this outcome in a remote store.
- [var taskOccurrenceIndex: Int](./ockanyoutcome/taskoccurrenceindex.md)
  A property that specifies how many events occured before this outcome became instantiated.
- [var taskUUID: UUID](./ockanyoutcome/taskuuid.md)
  A unique identifier for the specific version of the task that this outcome belongs to.
- [var values: [OCKOutcomeValue]](./ockanyoutcome/values.md)
  An array of values associated with this outcome.
### Instance Methods
- [func belongs(to: OCKAnyTask) -> Bool](./ockanyoutcome/belongs%28to%29.md)
  Determines if this outcome is associated with the given task.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKHealthKitOutcome](./ockhealthkitoutcome.md)
- [OCKOutcome](./ockoutcome.md)

## See Also

### Outcomes
- [struct OCKOutcome](./ockoutcome.md)
  An `OCKOutcome` represents the outcome of an event corresponding to a task. An outcome may have 0 or more values associated with it. For example, a task that asks a patient to measure their temperature will have events whose outcome will contain a single value representing the patient’s temperature.
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
- [struct OCKOutcomeQuery](./ockoutcomequery.md)
  A query that limits which outcomes will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyoutcome)*