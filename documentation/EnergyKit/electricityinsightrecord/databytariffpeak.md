# dataByTariffPeak

**Framework**: EnergyKit  
**Kind**: property

The electrical energy consumed or generated, or the runtime duration split out by tariff peaks, if available.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var dataByTariffPeak: ElectricityInsightRecord<Measure>.TariffPeak?
```

## Mentions

- [Providing charging history for electric vehicles](providing-informative-charging-history-for-electric-vehicles.md)

#### Discussion

The tariff peaks are the times of day when electricity prices are highest.

## See Also

- [ElectricityInsightRecord.TariffPeak](electricityinsightrecord/tariffpeak.md)
  A struct describing energy tariff peaks or duration data, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/databytariffpeak)*