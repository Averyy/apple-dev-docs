# ElectricVehicleChargingReason.IdleReason

**Framework**: EnergyKit  
**Kind**: enum

Information about why a vehicle remains idle when connected to a charger.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum IdleReason
```

## Mentions

- [Providing charging history for electric vehicles](providing-informative-charging-history-for-electric-vehicles.md)

#### Overview

Use these reasons with [`ElectricVehicleStatusEvent.Status.chargingIdle(_:)`](electricvehiclestatusevent/status-swift.enum/chargingidle(_:).md) to explain why charging hasn’t started or why it’s paused.

## Topics

### Charging targets reached
- [ElectricVehicleChargingReason.IdleReason.targetStateOfChargeReached](electricvehiclechargingreason/idlereason/targetstateofchargereached.md)
  A reason that indicates charging stops because the vehicle reaches its target state of charge.
- [ElectricVehicleChargingReason.IdleReason.batteryFull](electricvehiclechargingreason/idlereason/batteryfull.md)
  A reason that indicates charging stops because the battery is full.
- [ElectricVehicleChargingReason.IdleReason.targetAlreadyReached](electricvehiclechargingreason/idlereason/targetalreadyreached.md)
  A reason that indicates charging doesn’t start because the vehicle is already charged to the target state.
### Scheduled conditions
- [ElectricVehicleChargingReason.IdleReason.scheduledEnd](electricvehiclechargingreason/idlereason/scheduledend.md)
  A reason that indicates charging stops at a scheduled end time.
- [ElectricVehicleChargingReason.IdleReason.scheduledPause](electricvehiclechargingreason/idlereason/scheduledpause.md)
  A reason that indicates charging pauses at a scheduled time.
### Grid and rate optimization
- [ElectricVehicleChargingReason.IdleReason.waitingForCleanerEnergy](electricvehiclechargingreason/idlereason/waitingforcleanerenergy.md)
  A reason that indicates the vehicle waits for cleaner energy to become available on the grid.
- [ElectricVehicleChargingReason.IdleReason.waitingForLowerElectricityRates](electricvehiclechargingreason/idlereason/waitingforlowerelectricityrates.md)
  A reason that indicates the vehicle waits for lower electricity rates to become available.
### User actions
- [ElectricVehicleChargingReason.IdleReason.userPaused](electricvehiclechargingreason/idlereason/userpaused.md)
  A reason that indicates a person manually pauses charging.
- [ElectricVehicleChargingReason.IdleReason.userStopped](electricvehiclechargingreason/idlereason/userstopped.md)
  A reason that indicates a person manually stops charging.
### System conditions
- [ElectricVehicleChargingReason.IdleReason.chargerFault](electricvehiclechargingreason/idlereason/chargerfault.md)
  A reason that indicates charging stops due to a charger fault.
- [ElectricVehicleChargingReason.IdleReason.demandResponseActive](electricvehiclechargingreason/idlereason/demandresponseactive.md)
  A reason that indicates charging pauses due to an active utility-demand response event.
- [ElectricVehicleChargingReason.IdleReason.batteryThermalManagement](electricvehiclechargingreason/idlereason/batterythermalmanagement.md)
  A reason that indicates charging pauses for battery thermal management.
- [ElectricVehicleChargingReason.IdleReason.batteryHealthManagement](electricvehiclechargingreason/idlereason/batteryhealthmanagement.md)
  A reason that indicates charging pauses for battery health management.
- [ElectricVehicleChargingReason.IdleReason.insufficientPower](electricvehiclechargingreason/idlereason/insufficientpower.md)
  A reason that indicates charging stops because insufficient power is available.
- [ElectricVehicleChargingReason.IdleReason.loadBalancing](electricvehiclechargingreason/idlereason/loadbalancing.md)
  A reason that indicates charging pauses due to load balancing with other electrical devices.
### Unspecified reason
- [ElectricVehicleChargingReason.IdleReason.unknown](electricvehiclechargingreason/idlereason/unknown.md)
  A reason that indicates the vehicle is idle for an unspecified or unavailable reason.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclechargingreason/idlereason)*