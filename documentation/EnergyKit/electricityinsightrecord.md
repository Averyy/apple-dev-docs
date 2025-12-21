# ElectricityInsightRecord

**Framework**: EnergyKit  
**Kind**: struct

A structure that provides environmental impact and cost insights for electricity usage over a specific time period.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct ElectricityInsightRecord<Measure> where Measure : ElectricityInsightMeasure
```

#### Overview

This structure provides electricity usage data categorized by environmental impact ([`ElectricityInsightRecord.GridCleanliness`](electricityinsightrecord/gridcleanliness.md)) and cost factors ([`ElectricityInsightRecord.TariffPeak`](electricityinsightrecord/tariffpeak.md)) for analysis and optimization.

The electricity usage data ([`dataByGridCleanliness`](electricityinsightrecord/databygridcleanliness.md)) refers to either energy consumption or generation measurements, or amounts of time that an electrical device is operational and consuming energy. The type of electricity usage data depends on the generic type parameter ([`ElectricityInsightMeasure`](electricityinsightmeasure.md)) for a given instance, which can be either:

- [`ElectricityInsightRecord`](electricityinsightrecord.md)<[`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement)<[`UnitEnergy`](https://developer.apple.com/documentation/Foundation/UnitEnergy)>>
- [`ElectricityInsightRecord`](electricityinsightrecord.md)<[`Duration`](https://developer.apple.com/documentation/Swift/Duration)>

## Topics

### Getting the grid data
- [ElectricityInsightRecord.GridCleanliness](electricityinsightrecord/gridcleanliness.md)
  A structure that describes the environmental impact of grid electricity during specific time periods.
- [var dataByGridCleanliness: ElectricityInsightRecord<Measure>.GridCleanliness?](electricityinsightrecord/databygridcleanliness.md)
  Energy consumption or production, or device operational runtime categorized by the cleanliness of the grid electricity.
### Getting the tariff peak data
- [ElectricityInsightRecord.TariffPeak](electricityinsightrecord/tariffpeak.md)
  A struct describing energy tariff peaks or duration data, if available.
- [var dataByTariffPeak: ElectricityInsightRecord<Measure>.TariffPeak?](electricityinsightrecord/databytariffpeak.md)
  The electrical energy consumed or generated, or the runtime duration split out by tariff peaks, if available.
### Getting the insight record data
- [var totalRuntime: Duration?](electricityinsightrecord/totalruntime.md)
  The total time that electricity-consuming devices actively ran.
- [let range: DateInterval](electricityinsightrecord/range.md)
  The time period that the insight record spans.
- [var totalEnergy: Measurement<UnitEnergy>?](electricityinsightrecord/totalenergy.md)
  The total electrical energy consumed or generated.

## See Also

- [actor ElectricityInsightService](electricityinsightservice.md)
  A service for retrieving insights about electricity consumption.
- [struct ElectricityInsightQuery](electricityinsightquery.md)
  A structure describing a query that you use to obtain environmental impact information in the form of electricity insight records.
- [protocol ElectricityInsightMeasure](electricityinsightmeasure.md)
  A protocol for types that can measure electricity usage data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord)*