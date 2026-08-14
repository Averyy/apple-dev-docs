# ElectricityInsightQuery.Options

**Framework**: EnergyKit  
**Kind**: struct

A set of options that specify optional information to include in electricity insight records returned from the insight service.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

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
- [let rawValue: UInt](electricityinsightquery/options-swift.struct/rawvalue.md)
  The raw value of the option set.
### Getting the optional query insights
- [static let cleanliness: ElectricityInsightQuery.Options](electricityinsightquery/options-swift.struct/cleanliness.md)
  A query that includes cleanliness insights.
- [static let tariff: ElectricityInsightQuery.Options](electricityinsightquery/options-swift.struct/tariff.md)
  A query that includes tariff-based insights.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [let options: ElectricityInsightQuery.Options](electricityinsightquery/options-swift.property.md)
  The optional information to include in returned electricity insight records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/options-swift.struct)*