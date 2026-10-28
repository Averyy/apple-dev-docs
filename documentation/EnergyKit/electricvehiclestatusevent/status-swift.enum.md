# ElectricVehicleStatusEvent.Status

**Framework**: EnergyKit  
**Kind**: enum  
**Role**: Enumeration

The status of an electric vehicle’s charger connection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
enum Status
```

## Overview

Status represents a discrete snapshot without providing information about the session’s continuity, which can pair with the [`ElectricVehicleLoadEvent`](../electricvehicleloadevent.md) that tracks session-based energy flow.

## Topics

### Connection states
- [ElectricVehicleStatusEvent.Status.chargerPluggedIn](./status-swift.enum/chargerpluggedin.md)
  A status that indicates when the charger connects to the vehicle.
- [ElectricVehicleStatusEvent.Status.chargerUnplugged](./status-swift.enum/chargerunplugged.md)
  A status that indicates when the charger disconnects from the vehicle.
### Charging states
- [case chargingActive(ElectricVehicleChargingReason.ActiveReason)](./status-swift.enum/chargingactive%28_%29.md)
  A status that indicates that the vehicle is actively charging.
- [case chargingIdle(ElectricVehicleChargingReason.IdleReason)](./status-swift.enum/chargingidle%28_%29.md)
  A status that indicates the charger is connected but the vehicle isn’t charging.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting status information
- [let status: ElectricVehicleStatusEvent.Status](./status-swift.property.md)
  The current status of the vehicle relative to charger connection.
- [let stateOfCharge: Int](./stateofcharge.md)
  A state of charge as a percentage at the time of the status event.
- [let energy: Measurement<UnitEnergy>](./energy.md)
  A state of charge in milliwatt-hours at the time of the status event.
- [let estimatedRange: Measurement<UnitLength>?](./estimatedrange.md)
  An estimated range of driving distance based on the current energy state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/status-swift.enum)*