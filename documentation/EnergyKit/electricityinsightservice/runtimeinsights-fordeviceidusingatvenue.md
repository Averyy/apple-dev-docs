# runtimeInsights(forDeviceID:using:atVenue:)

**Framework**: EnergyKit  
**Kind**: method

Returns records that provide insight into runtime of a given device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
final func runtimeInsights(forDeviceID deviceID: String, using query: ElectricityInsightQuery, atVenue energyVenueID: UUID) async throws -> AsyncStream<ElectricityInsightRecord<Duration>>
```

#### Return Value

An `AsyncStream` of [`ElectricityInsightRecord`](electricityinsightrecord.md)s containing `Duration` values for a given device.

#### Discussion

The system throws [`EnergyKitError.venueUnavailable`](energykiterror/venueunavailable.md) if a person provides an invalid [`EnergyVenue`](energyvenue.md) identifier. If another request is in progress, the system throws[`EnergyKitError.inProgress`](energykiterror/inprogress.md).

## Parameters

- `deviceID`: The device identifier to return  s for.
- `query`: The   to specify the results.
- `energyVenueID`: The   identifier to return  s for.

## See Also

- [func energyInsights(forDeviceID: String, using: ElectricityInsightQuery, atVenue: UUID) async throws -> AsyncStream<ElectricityInsightRecord<Measurement<UnitEnergy>>>](electricityinsightservice/energyinsights(fordeviceid:using:atvenue:).md)
  Returns data that provides insight into electrical usage for a given device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightservice/runtimeinsights(fordeviceid:using:atvenue:))*