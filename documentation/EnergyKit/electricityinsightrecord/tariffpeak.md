# ElectricityInsightRecord.TariffPeak

**Framework**: EnergyKit  
**Kind**: struct

A struct describing energy tariff peaks or duration data, if available.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct TariffPeak
```

## Topics

### Initializing the peak energy data
- [init(superOffPeak: Measure?, offPeak: Measure?, partialPeak: Measure?, onPeak: Measure?, criticalPeak: Measure?, unknown: Measure?)](electricityinsightrecord/tariffpeak/init(superoffpeak:offpeak:partialpeak:onpeak:criticalpeak:unknown:).md)
  Creates an instance of the energy peak data.
### Getting the peak energy data
- [var criticalPeak: Measure?](electricityinsightrecord/tariffpeak/criticalpeak.md)
  The duration of energy or runtime data during critical peak hours.
- [var offPeak: Measure?](electricityinsightrecord/tariffpeak/offpeak.md)
  The duration of energy or runtime data during off-peak hours.
- [var onPeak: Measure?](electricityinsightrecord/tariffpeak/onpeak.md)
  The duration of energy or runtime data during peak hours.
- [var partialPeak: Measure?](electricityinsightrecord/tariffpeak/partialpeak.md)
  The duration of energy or runtime data during partial peak hours.
- [var superOffPeak: Measure?](electricityinsightrecord/tariffpeak/superoffpeak.md)
  The duration of energy or runtime data during super off-peak hours.
- [var unknown: Measure?](electricityinsightrecord/tariffpeak/unknown.md)
  The unknown duration of energy or runtime data.

## See Also

- [var dataByTariffPeak: ElectricityInsightRecord<Measure>.TariffPeak?](electricityinsightrecord/databytariffpeak.md)
  The electrical energy consumed or generated, or the runtime duration split out by tariff peaks, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/tariffpeak)*