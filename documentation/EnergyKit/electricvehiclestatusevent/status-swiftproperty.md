# status

**Framework**: EnergyKit  
**Kind**: property

The current status of the vehicle relative to charger connection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let status: ElectricVehicleStatusEvent.Status
```

## See Also

- [ElectricVehicleStatusEvent.Status](electricvehiclestatusevent/status-swift.enum.md)
  The status of an electric vehicle’s charger connection.
- [let stateOfCharge: Int](electricvehiclestatusevent/stateofcharge.md)
  A state of charge as a percentage at the time of the status event.
- [let energy: Measurement<UnitEnergy>](electricvehiclestatusevent/energy.md)
  A state of charge in milliwatt-hours at the time of the status event.
- [let estimatedRange: Measurement<UnitLength>?](electricvehiclestatusevent/estimatedrange.md)
  An estimated range of driving distance based on the current energy state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/status-swift.property)*