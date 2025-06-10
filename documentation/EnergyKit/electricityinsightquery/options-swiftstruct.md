# ElectricityInsightQuery.Options

**Framework**: EnergyKit  
**Kind**: struct

A set of options that specify optional information to include in electricity insight records returned from the insight service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct Options
```

#### Overview

Using an empty [`ElectricityInsightQuery.Options`](electricityinsightquery/options-swift.struct.md) returns the total value  of [`ElectricityInsightRecord`](electricityinsightrecord.md) without cleanliness or tariff breakdown.

## Topics

### Creating an option set
- [init(rawValue: UInt)](electricityinsightquery/options-swift.struct/init(rawvalue:).md)
  Creates an option set with the given raw value.
- [let rawValue: UInt](electricityinsightquery/options-swift.struct/rawvalue-swift.property.md)
  The raw value of the option set.
### Getting the optional query insights
- [static let cleanliness: ElectricityInsightQuery.Options](electricityinsightquery/options-swift.struct/cleanliness.md)
  A query that includes cleanliness insights.
- [static let tariff: ElectricityInsightQuery.Options](electricityinsightquery/options-swift.struct/tariff.md)
  A query that includes tariff-based insights.
### Type Aliases
- [ElectricityInsightQuery.Options.ArrayLiteralElement](electricityinsightquery/options-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [ElectricityInsightQuery.Options.Element](electricityinsightquery/options-swift.struct/element.md)
  The element type of the option set.
- [ElectricityInsightQuery.Options.RawValue](electricityinsightquery/options-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](electricityinsightquery/options-swift.struct/equatable-implementations.md)
- [OptionSet Implementations](electricityinsightquery/options-swift.struct/optionset-implementations.md)
- [RawRepresentable Implementations](electricityinsightquery/options-swift.struct/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](electricityinsightquery/options-swift.struct/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [let options: ElectricityInsightQuery.Options](electricityinsightquery/options-swift.property.md)
  The optional information to include in returned electricity insight records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/options-swift.struct)*