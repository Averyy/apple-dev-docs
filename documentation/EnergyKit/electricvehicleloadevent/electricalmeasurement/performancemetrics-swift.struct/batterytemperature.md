# batteryTemperature

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

A battery pack temperature.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
let batteryTemperature: Measurement<UnitTemperature>?
```

## Discussion

The system sets this property to `nil` when temperature data is unavailable.

## See Also

### Getting performance data
- [let estimatedRange: Measurement<UnitLength>?](./estimatedrange.md)
  An estimate of how far the vehicle can travel based on the current state of charge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct/batterytemperature)*