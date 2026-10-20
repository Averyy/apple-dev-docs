# ElectricityInsightMeasure

**Framework**: EnergyKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for types that can measure electricity usage data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
protocol ElectricityInsightMeasure
```

#### Overview

The [`ElectricityInsightRecord`](./electricityinsightrecord.md) structure uses this protocol as its generic type parameter, and supports the types:

- [`ElectricityInsightRecord`](./electricityinsightrecord.md)<[`Measurement`](../Foundation/measurement.md)<[`UnitEnergy`](../Foundation/unitenergy.md)>>
- [`ElectricityInsightRecord`](./electricityinsightrecord.md)<[`Duration`](../Swift/duration.md)>

## See Also

### Electricity insights
- [actor ElectricityInsightService](./electricityinsightservice.md)
  A service for retrieving insights about electricity consumption.
- [struct ElectricityInsightQuery](./electricityinsightquery.md)
  A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.
- [struct ElectricityInsightRecord](./electricityinsightrecord.md)
  A structure that provides environmental impact and cost insights for electricity usage over a specific time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightmeasure)*