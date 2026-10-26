---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomevaluetype"
framework: "CareKit/CareKitStore"
---

# OCKOutcomeValueType

**Framework**: CareKit/CareKitStore  
**Kind**: enum  
**Role**: Enumeration

An enumerator specifying the types of values that can be saved to an `OCKStore`.

## Declaration

```swift
enum OCKOutcomeValueType
```

## Topics

### Enumeration Cases
- [OCKOutcomeValueType.binary](./ockoutcomevaluetype/binary.md)
- [OCKOutcomeValueType.boolean](./ockoutcomevaluetype/boolean.md)
- [OCKOutcomeValueType.date](./ockoutcomevaluetype/date.md)
- [OCKOutcomeValueType.double](./ockoutcomevaluetype/double.md)
- [OCKOutcomeValueType.integer](./ockoutcomevaluetype/integer.md)
- [OCKOutcomeValueType.text](./ockoutcomevaluetype/text.md)
### Initializers
- [init?(rawValue: String)](./ockoutcomevaluetype/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./ockoutcomevaluetype/equatable-implementations.md)
- [RawRepresentable Implementations](./ockoutcomevaluetype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable

## See Also

### Outcomes
- [struct OCKOutcome](./ockoutcome.md)
  An `OCKOutcome` represents the outcome of an event corresponding to a task. An outcome may have 0 or more values associated with it. For example, a task that asks a patient to measure their temperature will have events whose outcome will contain a single value representing the patient’s temperature.
- [protocol OCKAnyOutcome](./ockanyoutcome.md)
  A protocol that allows CareKit to query and display outcomes.
- [struct OCKOutcomeValue](./ockoutcomevalue.md)
  An `OCKOutcomeValue` is a representation of any response of measurement that a user gives in response to a task. The underlying type could be any of a number of types including integers, booleans, dates, text, and binary data, among others.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockoutcomevaluetype)*