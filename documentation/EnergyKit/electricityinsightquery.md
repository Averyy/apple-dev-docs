# ElectricityInsightQuery

**Framework**: EnergyKit  
**Kind**: struct

A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct ElectricityInsightQuery
```

## Topics

### Creating an insight query request
- [init(options: ElectricityInsightQuery.Options, range: DateInterval, granularity: ElectricityInsightQuery.Granularity, flowDirection: ElectricityFlowDirection)](electricityinsightquery/init(options:range:granularity:flowdirection:).md)
  Creates an electricity insight query request.
### Adding optional insight records
- [ElectricityInsightQuery.Options](electricityinsightquery/options-swift.struct.md)
  A set of options that specify optional information to include in electricity insight records returned from the insight service.
- [let options: ElectricityInsightQuery.Options](electricityinsightquery/options-swift.property.md)
  The optional information to include in returned electricity insight records.
### Getting the query request information
- [ElectricityInsightQuery.Granularity](electricityinsightquery/granularity-swift.enum.md)
  The specific temporal granularity of electricity insight records.
- [let granularity: ElectricityInsightQuery.Granularity](electricityinsightquery/granularity-swift.property.md)
  The temporal granularity for returned electricity insight records.
- [let flowDirection: ElectricityFlowDirection](electricityinsightquery/flowdirection.md)
  A property that specifies whether the response contains imported or exported energy.
- [let range: DateInterval](electricityinsightquery/range.md)
  The requested date range.
### Decoding
- [init(from: any Decoder) throws](electricityinsightquery/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](electricityinsightquery/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ElectricityInsightRecord](electricityinsightrecord.md)
  A structure that represents displayable environmental impact information for electricity usage.
- [actor ElectricityInsightService](electricityinsightservice.md)
  A service for retrieving insights about electricity consumption.
- [protocol ElectricityInsightMeasure](electricityinsightmeasure.md)
  A measurement of electricity consumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery)*