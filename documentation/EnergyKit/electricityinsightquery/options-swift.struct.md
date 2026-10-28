# ElectricityInsightQuery.Options

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

A set of options that specify optional information to include in electricity insight records returned from the insight service.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct Options
```

## Overview

Using an empty [`ElectricityInsightQuery.Options`](./options-swift.struct.md) returns the total value  of [`ElectricityInsightRecord`](../electricityinsightrecord.md) without cleanliness or tariff breakdown.

## Topics

### Creating an option set
- [init(rawValue: UInt)](./options-swift.struct/init%28rawvalue%29.md)
  Creates an option set with the given raw value.
- [let rawValue: UInt](./options-swift.struct/rawvalue.md)
  The raw value of the option set.
### Getting the optional query insights
- [static let cleanliness: ElectricityInsightQuery.Options](./options-swift.struct/cleanliness.md)
  A query that includes cleanliness insights.
- [static let tariff: ElectricityInsightQuery.Options](./options-swift.struct/tariff.md)
  A query that includes tariff-based insights.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Adding optional insight records
- [let options: ElectricityInsightQuery.Options](./options-swift.property.md)
  The optional information to include in returned electricity insight records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery/options-swift.struct)*