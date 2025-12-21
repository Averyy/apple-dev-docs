# stateOfCharge

**Framework**: EnergyKit  
**Kind**: property

The remaining capacity available in a battery An integer ranging from `0` to `100` that’s proportional to the percentage of remaining capacity available in the battery where `0` and `100` correspond to the min and max state of charge respectively.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
let stateOfCharge: Int
```

#### Discussion

- `0`: empty
- `100`: full.

## See Also

- [let direction: ElectricityFlowDirection](electricvehicleloadevent/electricalmeasurement/direction.md)
  The electricity being imported or exported to the grid.
- [let energy: Measurement<UnitEnergy>](electricvehicleloadevent/electricalmeasurement/energy.md)
  The reported cumulative energy in milli-watt-hours [mWh] Accumulator is reset on `Session.State.end` The cummulative energy in milli-watt-hours [mWh] of the reporting device rounded to the nearest integer.
- [let power: Measurement<UnitPower>](electricvehicleloadevent/electricalmeasurement/power.md)
  The instantaneous power in milli-watts [mW] of the reporting device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/stateofcharge)*