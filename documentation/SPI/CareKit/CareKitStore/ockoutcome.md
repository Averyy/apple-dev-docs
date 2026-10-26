---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcome"
framework: "CareKit/CareKitStore"
---

# OCKOutcome

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An `OCKOutcome` represents the outcome of an event corresponding to a task. An outcome may have 0 or more values associated with it. For example, a task that asks a patient to measure their temperature will have events whose outcome will contain a single value representing the patient’s temperature.

## Declaration

```swift
struct OCKOutcome
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockoutcome/init%28from%29.md)
- [init(taskUUID: UUID, taskOccurrenceIndex: Int, values: [OCKOutcomeValue])](./ockoutcome/init%28taskuuid,taskoccurrenceindex,values%29.md)
  Initialize by specifying the version of the task that owns this outcome, how many events have occurred before this outcome, and the values.
### Instance Properties
- [var asset: String?](./ockoutcome/asset.md)
- [var createdDate: Date?](./ockoutcome/createddate.md)
- [var deletedDate: Date?](./ockoutcome/deleteddate.md)
- [var effectiveDate: Date](./ockoutcome/effectivedate.md)
- [var groupIdentifier: String?](./ockoutcome/groupidentifier.md)
- [var id: String](./ockoutcome/id.md)
- [var nextVersionUUIDs: [UUID]](./ockoutcome/nextversionuuids.md)
- [var notes: [OCKNote]?](./ockoutcome/notes.md)
- [var previousVersionUUIDs: [UUID]](./ockoutcome/previousversionuuids.md)
- [var remoteID: String?](./ockoutcome/remoteid.md)
- [var schemaVersion: OCKSemanticVersion?](./ockoutcome/schemaversion.md)
- [var source: String?](./ockoutcome/source.md)
- [var tags: [String]?](./ockoutcome/tags.md)
- [var taskOccurrenceIndex: Int](./ockoutcome/taskoccurrenceindex.md)
- [var taskUUID: UUID](./ockoutcome/taskuuid.md)
  The version ID of the task to which this outcomes belongs.
- [var timezone: TimeZone](./ockoutcome/timezone.md)
- [var updatedDate: Date?](./ockoutcome/updateddate.md)
- [var userInfo: [String : String]?](./ockoutcome/userinfo.md)
- [var uuid: UUID](./ockoutcome/uuid.md)
- [var values: [OCKOutcomeValue]](./ockoutcome/values.md)
### Instance Methods
- [func belongs(to: OCKAnyTask) -> Bool](./ockoutcome/belongs%28to%29.md)
### Default Implementations
- [Equatable Implementations](./ockoutcome/equatable-implementations.md)

## Relationships

### Conforms To
- [OCKAnyOutcome](./ockanyoutcome.md)
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Outcomes
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
- [struct OCKOutcomeQuery](./ockoutcomequery.md)
  A query that limits which outcomes will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcome)*