---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitoutcome"
framework: "CareKit/CareKitStore"
---

# OCKHealthKitOutcome

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct OCKHealthKitOutcome
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockhealthkitoutcome/init%28from%29.md)
- [init(taskUUID: UUID, taskOccurrenceIndex: Int, values: [OCKOutcomeValue])](./ockhealthkitoutcome/init%28taskuuid,taskoccurrenceindex,values%29.md)
  Initialize by specifying the version of the task that owns this outcome, how many events have occurred before this outcome, and the values.
### Instance Properties
- [var groupIdentifier: String?](./ockhealthkitoutcome/groupidentifier.md)
- [var id: String](./ockhealthkitoutcome/id.md)
- [let isOwnedByApp: Bool](./ockhealthkitoutcome/isownedbyapp.md)
  Denotes whether or not this outcome can be deleted from HealthKit.
- [var notes: [OCKNote]?](./ockhealthkitoutcome/notes.md)
- [var remoteID: String?](./ockhealthkitoutcome/remoteid.md)
- [var taskOccurrenceIndex: Int](./ockhealthkitoutcome/taskoccurrenceindex.md)
- [var taskUUID: UUID](./ockhealthkitoutcome/taskuuid.md)
  The UUID of the task to which this outcome belongs.
- [var values: [OCKOutcomeValue]](./ockhealthkitoutcome/values.md)
### Instance Methods
- [func belongs(to: OCKAnyTask) -> Bool](./ockhealthkitoutcome/belongs%28to%29.md)
### Default Implementations
- [Equatable Implementations](./ockhealthkitoutcome/equatable-implementations.md)

## Relationships

### Conforms To
- [OCKAnyOutcome](./ockanyoutcome.md)
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Identifiable
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
- [protocol OCKOutcomeStore](./ockoutcomestore.md)
- [protocol OCKAnyOutcomeStore](./ockanyoutcomestore.md)
- [protocol OCKReadableOutcomeStore](./ockreadableoutcomestore.md)
  A store that allows for reading outcomes.
- [protocol OCKAnyReadOnlyOutcomeStore](./ockanyreadonlyoutcomestore.md)
  A store that allows for reading outcomes.
- [struct OCKOutcomeQuery](./ockoutcomequery.md)
  A query that limits which outcomes will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitoutcome)*