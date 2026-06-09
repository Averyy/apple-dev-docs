# init(estimatedRange:batteryTemperature:)

**Framework**: EnergyKit  
**Kind**: init

Creates performance metrics for the current measurement.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(estimatedRange: Measurement<UnitLength>? = nil, batteryTemperature: Measurement<UnitTemperature>? = nil)
```

## Parameters

- `estimatedRange`: The estimated range of driving distance based on the current energy state, or `nil` if an estimate is unavailable.
- `batteryTemperature`: The battery pack temperature, or `nil` if the temperature is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct/init(estimatedrange:batterytemperature:))*