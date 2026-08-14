# ElectricityInsightQuery

**Framework**: EnergyKit  
**Kind**: struct

A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

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

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [actor ElectricityInsightService](electricityinsightservice.md)
  A service for retrieving insights about electricity consumption.
- [struct ElectricityInsightRecord](electricityinsightrecord.md)
  A structure that provides environmental impact and cost insights for electricity usage over a specific time period.
- [protocol ElectricityInsightMeasure](electricityinsightmeasure.md)
  A protocol for types that can measure electricity usage data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightquery)*