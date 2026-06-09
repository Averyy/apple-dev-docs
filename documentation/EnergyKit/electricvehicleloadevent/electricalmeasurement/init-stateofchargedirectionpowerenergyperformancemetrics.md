# init(stateOfCharge:direction:power:energy:performanceMetrics:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electrical measurement with optional performance metrics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(stateOfCharge: Int, direction: ElectricityFlowDirection, power: Measurement<UnitPower>, energy: Measurement<UnitEnergy>, performanceMetrics: ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics?)
```

## Parameters

- `stateOfCharge`: The remaining capacity available in the battery as a percentage (0-100).
- `direction`: The direction of electricity flow.
- `power`: The instantaneous power in milliwatts.
- `energy`: The accumulated electrical energy in milliwatt-hours.
- `performanceMetrics`: Performance metrics for this measurement, or `nil` if the metrics are unavailable.

## See Also

- [init(stateOfCharge: Int, direction: ElectricityFlowDirection, power: Measurement<UnitPower>, energy: Measurement<UnitEnergy>)](electricvehicleloadevent/electricalmeasurement/init(stateofcharge:direction:power:energy:).md)
  Initializes an electrical measurement for the electrical load event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/init(stateofcharge:direction:power:energy:performancemetrics:))*