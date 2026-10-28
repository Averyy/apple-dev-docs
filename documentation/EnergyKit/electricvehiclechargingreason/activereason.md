# ElectricVehicleChargingReason.ActiveReason

**Framework**: EnergyKit  
**Kind**: enum  
**Role**: Enumeration

Information about why a vehicle is actively charging.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
enum ActiveReason
```

## Overview

Use these reasons with [`ElectricVehicleStatusEvent.Status.chargingActive(_:)`](../electricvehiclestatusevent/status-swift.enum/chargingactive%28_%29.md) to explain why charging starts or resumes.

## Topics

### Grid and rate optimization
- [ElectricVehicleChargingReason.ActiveReason.cleanerEnergyAvailable](./activereason/cleanerenergyavailable.md)
  A reason that indicates charging starts because cleaner energy becomes available on the grid.
- [ElectricVehicleChargingReason.ActiveReason.lowerElectricityRatesAvailable](./activereason/lowerelectricityratesavailable.md)
  A reason that indicates charging starts because lower electricity rates become available.
### User actions
- [ElectricVehicleChargingReason.ActiveReason.userInitiated](./activereason/userinitiated.md)
  A reason that indicates a person manually starts charging.
- [ElectricVehicleChargingReason.ActiveReason.userResumed](./activereason/userresumed.md)
  A reason that indicates a person manually resumes charging after pausing.
### Scheduled charging
- [ElectricVehicleChargingReason.ActiveReason.scheduledStart](./activereason/scheduledstart.md)
  A reason that indicates charging starts at a scheduled time.
- [ElectricVehicleChargingReason.ActiveReason.scheduledResume](./activereason/scheduledresume.md)
  A reason that indicates charging resumes at a scheduled time after pausing.
### System conditions resolved
- [ElectricVehicleChargingReason.ActiveReason.demandResponseEnded](./activereason/demandresponseended.md)
  A reason that indicates charging starts because a utility-demand response event ends.
- [ElectricVehicleChargingReason.ActiveReason.batteryThermalManagementCompleted](./activereason/batterythermalmanagementcompleted.md)
  A reason that indicates charging starts after battery thermal management completes.
- [ElectricVehicleChargingReason.ActiveReason.batteryHealthManagementCompleted](./activereason/batteryhealthmanagementcompleted.md)
  A reason that indicates charging starts after battery health management completes.
- [ElectricVehicleChargingReason.ActiveReason.chargerFaultCleared](./activereason/chargerfaultcleared.md)
  A reason that indicates charging starts after a charger fault resolves.
- [ElectricVehicleChargingReason.ActiveReason.sufficientPowerRestored](./activereason/sufficientpowerrestored.md)
  A reason that indicates charging starts after sufficient power becomes available.
- [ElectricVehicleChargingReason.ActiveReason.loadBalancingCompleted](./activereason/loadbalancingcompleted.md)
  A reason that indicates charging starts after load-balancing completes.
### Unspecified reason
- [ElectricVehicleChargingReason.ActiveReason.unknown](./activereason/unknown.md)
  A reason that indicates charging starts for an unspecified or unavailable reason.

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

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclechargingreason/activereason)*