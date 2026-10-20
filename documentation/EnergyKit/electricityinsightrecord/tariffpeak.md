# ElectricityInsightRecord.TariffPeak

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

A struct describing energy tariff peaks or duration data, if available.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct TariffPeak
```

## Topics

### Initializing the peak energy data
- [init(superOffPeak: Measure?, offPeak: Measure?, partialPeak: Measure?, onPeak: Measure?, criticalPeak: Measure?, unknown: Measure?)](./tariffpeak/init%28superoffpeak,offpeak,partialpeak,onpeak,criticalpeak,unknown%29.md)
  Creates an instance of the energy peak data.
### Getting the peak energy data
- [var criticalPeak: Measure?](./tariffpeak/criticalpeak.md)
  The duration of energy or runtime data during critical peak hours.
- [var offPeak: Measure?](./tariffpeak/offpeak.md)
  The duration of energy or runtime data during off-peak hours.
- [var onPeak: Measure?](./tariffpeak/onpeak.md)
  The duration of energy or runtime data during peak hours.
- [var partialPeak: Measure?](./tariffpeak/partialpeak.md)
  The duration of energy or runtime data during partial peak hours.
- [var superOffPeak: Measure?](./tariffpeak/superoffpeak.md)
  The duration of energy or runtime data during super off-peak hours.
- [var unknown: Measure?](./tariffpeak/unknown.md)
  The unknown duration of energy or runtime data.

## See Also

### Getting the tariff peak data
- [var dataByTariffPeak: ElectricityInsightRecord<Measure>.TariffPeak?](./databytariffpeak.md)
  The electrical energy consumed or generated, or the runtime duration split out by tariff peaks, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityinsightrecord/tariffpeak)*