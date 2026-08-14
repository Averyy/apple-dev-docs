# dataByGridCleanliness

**Framework**: EnergyKit  
**Kind**: property

Energy consumption or production, or device operational runtime categorized by the cleanliness of the grid electricity.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst ?+

## Declaration

```swift
var dataByGridCleanliness: ElectricityInsightRecord<Measure>.GridCleanliness?
```

## Mentions

- [Providing charging history for electric vehicles](providing-informative-charging-history-for-electric-vehicles.md)

#### Discussion

This property returns electricity usage data organized by how environmentally friendly the production of the energy is. The electricity usage data refers to either energy consumption or generation measurements, or amounts of time that an electrical device is operational and consuming energy. The type of the returned value depends on the insight record’s generic type parameter:

- [`ElectricityInsightRecord`](electricityinsightrecord.md)<[`Measurement`](https://developer.apple.com/documentation/foundation/measurement)<[`UnitEnergy`](https://developer.apple.com/documentation/foundation/unitenergy)>> instances return [`Measurement`](https://developer.apple.com/documentation/foundation/measurement)<[`UnitEnergy`](https://developer.apple.com/documentation/foundation/unitenergy)> for this property.
- [`ElectricityInsightRecord`](electricityinsightrecord.md)<[`Duration`](https://developer.apple.com/documentation/swift/duration)> instances return [`Duration`](https://developer.apple.com/documentation/swift/duration) for this property.

## See Also

- [ElectricityInsightRecord.GridCleanliness](electricityinsightrecord/gridcleanliness.md)
  A structure that describes the environmental impact of grid electricity during specific time periods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/databygridcleanliness)*