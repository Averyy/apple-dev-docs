# energy

**Framework**: EnergyKit  
**Kind**: property

A state of charge in milliwatt-hours at the time of the status event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let energy: Measurement<UnitEnergy>
```

## See Also

- [let status: ElectricVehicleStatusEvent.Status](electricvehiclestatusevent/status-swift.property.md)
  The current status of the vehicle relative to charger connection.
- [ElectricVehicleStatusEvent.Status](electricvehiclestatusevent/status-swift.enum.md)
  The status of an electric vehicle’s charger connection.
- [let stateOfCharge: Int](electricvehiclestatusevent/stateofcharge.md)
  A state of charge as a percentage at the time of the status event.
- [let estimatedRange: Measurement<UnitLength>?](electricvehiclestatusevent/estimatedrange.md)
  An estimated range of driving distance based on the current energy state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/energy)*