# ElectricityInsightRecord.GridCleanliness

**Framework**: EnergyKit  
**Kind**: struct

A structure that describes the environmental impact of grid electricity during specific time periods.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst ?+

## Declaration

```swift
struct GridCleanliness
```

#### Overview

The [`ElectricityInsightRecord`](electricityinsightrecord.md) structure’s [`dataByGridCleanliness`](electricityinsightrecord/databygridcleanliness.md) property returns electricity usage by the categories that this structure defines.

The type of electricity usage that this structure stores depends on the generic type parameter of a given [`ElectricityInsightMeasure`](electricityinsightmeasure.md) instance. If the generic type is:

- **[`Measurement`](https://developer.apple.com/documentation/Foundation/Measurement)<[`UnitEnergy`](https://developer.apple.com/documentation/Foundation/UnitEnergy)>**: The electricity usage refers to energy consumption or generation.
- **[`Duration`](https://developer.apple.com/documentation/Swift/Duration)**: The electricity usage refers to an amount of time that an electrical device is operational and consuming energy.

## Topics

### Initializing the grid data
- [init(cleaner: Measure?, lessClean: Measure?, avoid: Measure?, unknown: Measure?)](electricityinsightrecord/gridcleanliness/init(cleaner:lessclean:avoid:unknown:).md)
  Initializes the collection of grid cleanliness data.
### Getting grid cleanliness information
- [var cleaner: Measure?](electricityinsightrecord/gridcleanliness/cleaner.md)
  A category for electricity usage during the cleanest grid periods.
- [var lessClean: Measure?](electricityinsightrecord/gridcleanliness/lessclean.md)
  A category for electricity usage during less-clean grid periods.
- [var avoid: Measure?](electricityinsightrecord/gridcleanliness/avoid.md)
  A category for electricity usage during periods that the framework suggests a person avoid.
- [var unknown: Measure?](electricityinsightrecord/gridcleanliness/unknown.md)
  A category of electricity usage when grid cleanliness information is unavailable.

## See Also

- [var dataByGridCleanliness: ElectricityInsightRecord<Measure>.GridCleanliness?](electricityinsightrecord/databygridcleanliness.md)
  Energy consumption or production, or device operational runtime categorized by the cleanliness of the grid electricity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/gridcleanliness)*