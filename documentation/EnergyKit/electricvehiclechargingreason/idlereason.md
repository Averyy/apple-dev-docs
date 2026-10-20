# ElectricVehicleChargingReason.IdleReason

**Framework**: EnergyKit  
**Kind**: enum  
**Role**: Enumeration

Information about why a vehicle remains idle when connected to a charger.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
enum IdleReason
```

## Mentions

- [Providing charging history for electric vehicles](../providing-informative-charging-history-for-electric-vehicles.md)

#### Overview

Use these reasons with [`ElectricVehicleStatusEvent.Status.chargingIdle(_:)`](../electricvehiclestatusevent/status-swift.enum/chargingidle%28_%29.md) to explain why charging hasn’t started or why it’s paused.

## Topics

### Charging targets reached
- [ElectricVehicleChargingReason.IdleReason.targetStateOfChargeReached](./idlereason/targetstateofchargereached.md)
  A reason that indicates charging stops because the vehicle reaches its target state of charge.
- [ElectricVehicleChargingReason.IdleReason.batteryFull](./idlereason/batteryfull.md)
  A reason that indicates charging stops because the battery is full.
- [ElectricVehicleChargingReason.IdleReason.targetAlreadyReached](./idlereason/targetalreadyreached.md)
  A reason that indicates charging doesn’t start because the vehicle is already charged to the target state.
### Scheduled conditions
- [ElectricVehicleChargingReason.IdleReason.scheduledEnd](./idlereason/scheduledend.md)
  A reason that indicates charging stops at a scheduled end time.
- [ElectricVehicleChargingReason.IdleReason.scheduledPause](./idlereason/scheduledpause.md)
  A reason that indicates charging pauses at a scheduled time.
### Grid and rate optimization
- [ElectricVehicleChargingReason.IdleReason.waitingForCleanerEnergy](./idlereason/waitingforcleanerenergy.md)
  A reason that indicates the vehicle waits for cleaner energy to become available on the grid.
- [ElectricVehicleChargingReason.IdleReason.waitingForLowerElectricityRates](./idlereason/waitingforlowerelectricityrates.md)
  A reason that indicates the vehicle waits for lower electricity rates to become available.
### User actions
- [ElectricVehicleChargingReason.IdleReason.userPaused](./idlereason/userpaused.md)
  A reason that indicates a person manually pauses charging.
- [ElectricVehicleChargingReason.IdleReason.userStopped](./idlereason/userstopped.md)
  A reason that indicates a person manually stops charging.
### System conditions
- [ElectricVehicleChargingReason.IdleReason.chargerFault](./idlereason/chargerfault.md)
  A reason that indicates charging stops due to a charger fault.
- [ElectricVehicleChargingReason.IdleReason.demandResponseActive](./idlereason/demandresponseactive.md)
  A reason that indicates charging pauses due to an active utility-demand response event.
- [ElectricVehicleChargingReason.IdleReason.batteryThermalManagement](./idlereason/batterythermalmanagement.md)
  A reason that indicates charging pauses for battery thermal management.
- [ElectricVehicleChargingReason.IdleReason.batteryHealthManagement](./idlereason/batteryhealthmanagement.md)
  A reason that indicates charging pauses for battery health management.
- [ElectricVehicleChargingReason.IdleReason.insufficientPower](./idlereason/insufficientpower.md)
  A reason that indicates charging stops because insufficient power is available.
- [ElectricVehicleChargingReason.IdleReason.loadBalancing](./idlereason/loadbalancing.md)
  A reason that indicates charging pauses due to load balancing with other electrical devices.
### Unspecified reason
- [ElectricVehicleChargingReason.IdleReason.unknown](./idlereason/unknown.md)
  A reason that indicates the vehicle is idle for an unspecified or unavailable reason.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclechargingreason/idlereason)*