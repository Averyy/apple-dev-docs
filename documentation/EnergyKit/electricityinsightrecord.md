# ElectricityInsightRecord

**Framework**: EnergyKit  
**Kind**: struct

A structure that represents displayable environmental impact information for electricity usage.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
struct ElectricityInsightRecord<Measure> where Measure : ElectricityInsightMeasure
```

#### Overview

The displayable information available for a given time period.

## Topics

### Getting the grid data
- [ElectricityInsightRecord.GridCleanliness](electricityinsightrecord/gridcleanliness.md)
  A struct that describes the cleanliness of the grid’s energy or duration data.
- [var dataByGridCleanliness: ElectricityInsightRecord<Measure>.GridCleanliness?](electricityinsightrecord/databygridcleanliness.md)
  The electrical energy consumed or generated, or the runtime duration broken down by levels of cleanliness.
### Getting the tariff peak data
- [ElectricityInsightRecord.TariffPeak](electricityinsightrecord/tariffpeak.md)
  A struct describing energy tariff peaks or duration data, if available.
- [var dataByTariffPeak: ElectricityInsightRecord<Measure>.TariffPeak?](electricityinsightrecord/databytariffpeak.md)
  The electrical energy consumed or generated, or the runtime duration split out by tariff peaks, if available.
### Getting the insight record data
- [var totalRuntime: Duration?](electricityinsightrecord/totalruntime.md)
  Represents the total runtime for the device in the date range.
- [let range: DateInterval](electricityinsightrecord/range.md)
  The date interval for which the system generates the insight.
- [var totalEnergy: Measurement<UnitEnergy>?](electricityinsightrecord/totalenergy.md)
  The total energy either consumed or generated in the date range.

## See Also

- [actor ElectricityInsightService](electricityinsightservice.md)
  A service for retrieving insights about electricity consumption.
- [struct ElectricityInsightQuery](electricityinsightquery.md)
  A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.
- [protocol ElectricityInsightMeasure](electricityinsightmeasure.md)
  A measurement of electricity consumption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord)*