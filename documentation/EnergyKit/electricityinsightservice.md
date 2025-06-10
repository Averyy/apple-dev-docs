# ElectricityInsightService

**Framework**: EnergyKit  
**Kind**: class

A service for retrieving insights about electricity consumption.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

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
### Instance Properties
- [var unownedExecutor: UnownedSerialExecutor](electricityinsightservice/unownedexecutor.md)
  Retrieve the executor for this actor as an optimized, unowned reference.
### Default Implementations
- [Actor Implementations](electricityinsightservice/actor-implementations.md)

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ElectricityInsightRecord](electricityinsightrecord.md)
  A structure that represents displayable environmental impact information for electricity usage.
- [struct ElectricityInsightQuery](electricityinsightquery.md)
  A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.
- [protocol ElectricityInsightMeasure](electricityinsightmeasure.md)
  A measurement of electricity consumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightservice)*