# ElectricVehicleStatusEvent.ChargingTarget

**Framework**: EnergyKit  
**Kind**: struct

The desired target when charging an electric vehicle.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct ChargingTarget
```

#### Overview

Charging targets represent a person’s intent, such as their desired state of charge or charging range, and planning data, such as their selected start time or estimated completion time. Combined, this information describes the desired outcome of a charging session.

Use charging target values when a person configures charging preferences in your app or when the vehicle supports scheduled charging features.

## Topics

### Creating charging targets
- [init(stateOfCharge: Int, estimatedCompletionTime: Date, scheduledStartTime: Date, estimatedRangeAtTarget: Measurement<UnitLength>?)](electricvehiclestatusevent/chargingtarget-swift.struct/init(stateofcharge:estimatedcompletiontime:scheduledstarttime:estimatedrangeattarget:).md)
  Creates target information for the desired outcome of charging an electric vehicle.
### Getting target information
- [let stateOfCharge: Int](electricvehiclestatusevent/chargingtarget-swift.struct/stateofcharge.md)
  Target state of charge for this charging session (0-100)
- [let estimatedCompletionTime: Date](electricvehiclestatusevent/chargingtarget-swift.struct/estimatedcompletiontime.md)
  An estimated time of when charging completes.
- [let scheduledStartTime: Date](electricvehiclestatusevent/chargingtarget-swift.struct/scheduledstarttime.md)
  A scheduled time for when charging starts.
- [let estimatedRangeAtTarget: Measurement<UnitLength>?](electricvehiclestatusevent/chargingtarget-swift.struct/estimatedrangeattarget.md)
  An estimated range of driving distance for the target state of charge.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let chargingTarget: ElectricVehicleStatusEvent.ChargingTarget?](electricvehiclestatusevent/chargingtarget-swift.property.md)
  The desired target when charging an electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/chargingtarget-swift.struct)*