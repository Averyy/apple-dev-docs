# power

**Framework**: EnergyKit  
**Kind**: property

The instantaneous power in milli-watts [mW] of the reporting device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
let power: Measurement<UnitPower>
```

## See Also

- [let direction: ElectricityFlowDirection](electricvehicleloadevent/electricalmeasurement/direction.md)
  The electricity being imported or exported to the grid.
- [let energy: Measurement<UnitEnergy>](electricvehicleloadevent/electricalmeasurement/energy.md)
  The reported cumulative energy in milli-watt-hours [mWh] Accumulator is reset on `Session.State.end` The cummulative energy in milli-watt-hours [mWh] of the reporting device rounded to the nearest integer.
- [let stateOfCharge: Int](electricvehicleloadevent/electricalmeasurement/stateofcharge.md)
  The remaining capacity available in a battery An integer ranging from `0` to `100` that’s proportional to the percentage of remaining capacity available in the battery where `0` and `100` correspond to the min and max state of charge respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/power)*