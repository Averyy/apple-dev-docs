# ElectricityInsightService

**Framework**: EnergyKit  
**Kind**: class

A service for retrieving insights about electricity consumption.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final actor ElectricityInsightService
```

## Topics

### Retrieving the shared instance
- [static let shared: ElectricityInsightService](electricityinsightservice/shared.md)
  A single, shared insight service object.
### Getting device insights
- [func energyInsights(forDeviceID: String, using: ElectricityInsightQuery, atVenue: UUID) async throws -> AsyncStream<ElectricityInsightRecord<Measurement<UnitEnergy>>>](electricityinsightservice/energyinsights(fordeviceid:using:atvenue:).md)
  Returns data that provides insight into electrical usage for a given device.
- [func runtimeInsights(forDeviceID: String, using: ElectricityInsightQuery, atVenue: UUID) async throws -> AsyncStream<ElectricityInsightRecord<Duration>>](electricityinsightservice/runtimeinsights(fordeviceid:using:atvenue:).md)
  Returns records that provide insight into runtime of a given device.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ElectricityInsightQuery](electricityinsightquery.md)
  A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.
- [struct ElectricityInsightRecord](electricityinsightrecord.md)
  A structure that provides environmental impact and cost insights for electricity usage over a specific time period.
- [protocol ElectricityInsightMeasure](electricityinsightmeasure.md)
  A protocol for types that can measure electricity usage data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightservice)*