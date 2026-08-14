# ElectricityInsightMeasure

**Framework**: EnergyKit  
**Kind**: protocol

A protocol for types that can measure electricity usage data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
protocol ElectricityInsightMeasure
```

#### Overview

The [`ElectricityInsightRecord`](electricityinsightrecord.md) structure uses this protocol as its generic type parameter, and supports the types:

- [`ElectricityInsightRecord`](electricityinsightrecord.md)<[`Measurement`](https://developer.apple.com/documentation/foundation/measurement)<[`UnitEnergy`](https://developer.apple.com/documentation/foundation/unitenergy)>>
- [`ElectricityInsightRecord`](electricityinsightrecord.md)<[`Duration`](https://developer.apple.com/documentation/swift/duration)>

## See Also

- [actor ElectricityInsightService](electricityinsightservice.md)
  A service for retrieving insights about electricity consumption.
- [struct ElectricityInsightQuery](electricityinsightquery.md)
  A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.
- [struct ElectricityInsightRecord](electricityinsightrecord.md)
  A structure that provides environmental impact and cost insights for electricity usage over a specific time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightmeasure)*