# ElectricVehicleChargingReason.ActiveReason

**Framework**: EnergyKit  
**Kind**: enum

Information about why a vehicle is actively charging.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum ActiveReason
```

#### Overview

Use these reasons with [`ElectricVehicleStatusEvent.Status.chargingActive(_:)`](electricvehiclestatusevent/status-swift.enum/chargingactive(_:).md) to explain why charging starts or resumes.

## Topics

### Grid and rate optimization
- [ElectricVehicleChargingReason.ActiveReason.cleanerEnergyAvailable](electricvehiclechargingreason/activereason/cleanerenergyavailable.md)
  A reason that indicates charging starts because cleaner energy becomes available on the grid.
- [ElectricVehicleChargingReason.ActiveReason.lowerElectricityRatesAvailable](electricvehiclechargingreason/activereason/lowerelectricityratesavailable.md)
  A reason that indicates charging starts because lower electricity rates become available.
### User actions
- [ElectricVehicleChargingReason.ActiveReason.userInitiated](electricvehiclechargingreason/activereason/userinitiated.md)
  A reason that indicates a person manually starts charging.
- [ElectricVehicleChargingReason.ActiveReason.userResumed](electricvehiclechargingreason/activereason/userresumed.md)
  A reason that indicates a person manually resumes charging after pausing.
### Scheduled charging
- [ElectricVehicleChargingReason.ActiveReason.scheduledStart](electricvehiclechargingreason/activereason/scheduledstart.md)
  A reason that indicates charging starts at a scheduled time.
- [ElectricVehicleChargingReason.ActiveReason.scheduledResume](electricvehiclechargingreason/activereason/scheduledresume.md)
  A reason that indicates charging resumes at a scheduled time after pausing.
### System conditions resolved
- [ElectricVehicleChargingReason.ActiveReason.demandResponseEnded](electricvehiclechargingreason/activereason/demandresponseended.md)
  A reason that indicates charging starts because a utility-demand response event ends.
- [ElectricVehicleChargingReason.ActiveReason.batteryThermalManagementCompleted](electricvehiclechargingreason/activereason/batterythermalmanagementcompleted.md)
  A reason that indicates charging starts after battery thermal management completes.
- [ElectricVehicleChargingReason.ActiveReason.batteryHealthManagementCompleted](electricvehiclechargingreason/activereason/batteryhealthmanagementcompleted.md)
  A reason that indicates charging starts after battery health management completes.
- [ElectricVehicleChargingReason.ActiveReason.chargerFaultCleared](electricvehiclechargingreason/activereason/chargerfaultcleared.md)
  A reason that indicates charging starts after a charger fault resolves.
- [ElectricVehicleChargingReason.ActiveReason.sufficientPowerRestored](electricvehiclechargingreason/activereason/sufficientpowerrestored.md)
  A reason that indicates charging starts after sufficient power becomes available.
- [ElectricVehicleChargingReason.ActiveReason.loadBalancingCompleted](electricvehiclechargingreason/activereason/loadbalancingcompleted.md)
  A reason that indicates charging starts after load-balancing completes.
### Unspecified reason
- [ElectricVehicleChargingReason.ActiveReason.unknown](electricvehiclechargingreason/activereason/unknown.md)
  A reason that indicates charging starts for an unspecified or unavailable reason.

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

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclechargingreason/activereason)*