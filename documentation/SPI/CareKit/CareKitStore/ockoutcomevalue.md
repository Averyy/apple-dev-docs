---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomevalue"
framework: "CareKit/CareKitStore"
---

# OCKOutcomeValue

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

An `OCKOutcomeValue` is a representation of any response of measurement that a user gives in response to a task. The underlying type could be any of a number of types including integers, booleans, dates, text, and binary data, among others.

## Declaration

```swift
struct OCKOutcomeValue
```

## Mentions

- [Creating schedules for tasks](./creating-schedules-for-tasks.md)

## Topics

### Operators
- [static func == (OCKOutcomeValue, OCKOutcomeValue) -> Bool](./ockoutcomevalue/eqeq%28_,_%29.md)
### Initializers
- [init(OCKOutcomeValueUnderlyingType, units: String?)](./ockoutcomevalue/init%28_,units%29.md)
  Initialize by specifying a value and an optional unit
- [init(from: Decoder) throws](./ockoutcomevalue/init%28from%29.md)
### Instance Properties
- [var booleanValue: Bool?](./ockoutcomevalue/booleanvalue.md)
  The underlying value as a boolean.
- [var createdDate: Date](./ockoutcomevalue/createddate.md)
  The date that this value was created.
- [var dataValue: Data?](./ockoutcomevalue/datavalue.md)
  The underlying value as binary data.
- [var dateValue: Date?](./ockoutcomevalue/datevalue.md)
  The underlying value as a date.
- [var description: String](./ockoutcomevalue/description.md)
- [var doubleValue: Double?](./ockoutcomevalue/doublevalue.md)
  The underlying value as a floating point number.
- [var integerValue: Int?](./ockoutcomevalue/integervalue.md)
  The underlying value as an integer.
- [var kind: String?](./ockoutcomevalue/kind.md)
  An optional property that can be used to specify what kind of value this is (e.g. blood pressure, qualitative stress, weight)
- [var numberValue: NSNumber?](./ockoutcomevalue/numbervalue.md)
- [var stringValue: String?](./ockoutcomevalue/stringvalue.md)
  The underlying value as text.
- [var type: OCKOutcomeValueType](./ockoutcomevalue/type.md)
  Holds information about the type of this value.
- [var units: String?](./ockoutcomevalue/units.md)
  The units for this measurement.
- [var value: OCKOutcomeValueUnderlyingType](./ockoutcomevalue/value.md)
  The underlying value.
### Instance Methods
- [func encode(to: Encoder) throws](./ockoutcomevalue/encode%28to%29.md)
- [func hash(into: inout Hasher)](./ockoutcomevalue/hash%28into%29.md)
### Default Implementations
- [Equatable Implementations](./ockoutcomevalue/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Outcomes
- [struct OCKOutcome](./ockoutcome.md)
  An `OCKOutcome` represents the outcome of an event corresponding to a task. An outcome may have 0 or more values associated with it. For example, a task that asks a patient to measure their temperature will have events whose outcome will contain a single value representing the patient’s temperature.
- [protocol OCKAnyOutcome](./ockanyoutcome.md)
  A protocol that allows CareKit to query and display outcomes.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomevalue)*