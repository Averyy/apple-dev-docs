# energy

**Framework**: EnergyKit  
**Kind**: property

The cumulative energy in milli-watt-hours [mWh] of the reporting device rounded to the nearest integer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
let energy: Measurement<UnitEnergy>
```

#### Discussion

The accumulator is reset on [`ElectricVehicleLoadEvent.Session.State.end`](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md).

## See Also

- [let stateOfCharge: Int](electricvehicleloadevent/electricalmeasurement/stateofcharge.md)
  The remaining capacity available in a battery An integer ranging from `0` to `100` that’s proportional to the percentage of remaining capacity available in the battery where `0` and `100` correspond to the min and max state of charge respectively.
- [let direction: ElectricityFlowDirection](electricvehicleloadevent/electricalmeasurement/direction.md)
  The electricity being imported or exported to the grid.
- [let power: Measurement<UnitPower>](electricvehicleloadevent/electricalmeasurement/power.md)
  The instantaneous power in milli-watts [mW] of the reporting device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/energy)*