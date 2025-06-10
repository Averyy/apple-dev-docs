# dataByTariffPeak

**Framework**: EnergyKit  
**Kind**: property

The electrical energy consumed or generated, or the runtime duration split out by tariff peaks, if available.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
var dataByTariffPeak: ElectricityInsightRecord<Measure>.TariffPeak?
```

#### Discussion

The tariff peaks are the times of day when electricity prices are highest.

## See Also

- [ElectricityInsightRecord.TariffPeak](electricityinsightrecord/tariffpeak.md)
  A struct describing energy tariff peaks or duration data, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/databytariffpeak)*