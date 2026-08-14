# ElectricVehicleStatusEvent.Status

**Framework**: EnergyKit  
**Kind**: enum

The status of an electric vehicle’s charger connection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Status
```

#### Overview

Status represents a discrete snapshot without providing information about the session’s continuity, which can pair with the [`ElectricVehicleLoadEvent`](electricvehicleloadevent.md) that tracks session-based energy flow.

## Topics

### Connection states
- [ElectricVehicleStatusEvent.Status.chargerPluggedIn](electricvehiclestatusevent/status-swift.enum/chargerpluggedin.md)
  A status that indicates when the charger connects to the vehicle.
- [ElectricVehicleStatusEvent.Status.chargerUnplugged](electricvehiclestatusevent/status-swift.enum/chargerunplugged.md)
  A status that indicates when the charger disconnects from the vehicle.
### Charging states
- [case chargingActive(ElectricVehicleChargingReason.ActiveReason)](electricvehiclestatusevent/status-swift.enum/chargingactive(_:).md)
  A status that indicates that the vehicle is actively charging.
- [case chargingIdle(ElectricVehicleChargingReason.IdleReason)](electricvehiclestatusevent/status-swift.enum/chargingidle(_:).md)
  A status that indicates the charger is connected but the vehicle isn’t charging.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let status: ElectricVehicleStatusEvent.Status](electricvehiclestatusevent/status-swift.property.md)
  The current status of the vehicle relative to charger connection.
- [let stateOfCharge: Int](electricvehiclestatusevent/stateofcharge.md)
  A state of charge as a percentage at the time of the status event.
- [let energy: Measurement<UnitEnergy>](electricvehiclestatusevent/energy.md)
  A state of charge in milliwatt-hours at the time of the status event.
- [let estimatedRange: Measurement<UnitLength>?](electricvehiclestatusevent/estimatedrange.md)
  An estimated range of driving distance based on the current energy state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/status-swift.enum)*