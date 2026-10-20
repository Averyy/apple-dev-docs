# direction

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

The electricity being imported or exported to the grid.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
let direction: ElectricityFlowDirection
```

## See Also

### Getting electrical measurements
- [let stateOfCharge: Int](./stateofcharge.md)
  The remaining capacity available in a battery An integer ranging from `0` to `100` that’s proportional to the percentage of remaining capacity available in the battery where `0` and `100` correspond to the min and max state of charge respectively.
- [let power: Measurement<UnitPower>](./power.md)
  The instantaneous power in milli-watts [mW] of the reporting device.
- [let energy: Measurement<UnitEnergy>](./energy.md)
  The cumulative energy in milli-watt-hours [mWh] of the reporting device rounded to the nearest integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/direction)*