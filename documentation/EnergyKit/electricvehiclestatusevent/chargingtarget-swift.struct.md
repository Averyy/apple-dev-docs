# ElectricVehicleStatusEvent.ChargingTarget

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

The desired target when charging an electric vehicle.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
struct ChargingTarget
```

#### Overview

Charging targets represent a person’s intent, such as their desired state of charge or charging range, and planning data, such as their selected start time or estimated completion time. Combined, this information describes the desired outcome of a charging session.

Use charging target values when a person configures charging preferences in your app or when the vehicle supports scheduled charging features.

## Topics

### Creating charging targets
- [init(stateOfCharge: Int, estimatedCompletionTime: Date, scheduledStartTime: Date, estimatedRangeAtTarget: Measurement<UnitLength>?)](./chargingtarget-swift.struct/init%28stateofcharge,estimatedcompletiontime,scheduledstarttime,estimatedrangeattarget%29.md)
  Creates target information for the desired outcome of charging an electric vehicle.
### Getting target information
- [let stateOfCharge: Int](./chargingtarget-swift.struct/stateofcharge.md)
  Target state of charge for this charging session (0-100)
- [let estimatedCompletionTime: Date](./chargingtarget-swift.struct/estimatedcompletiontime.md)
  An estimated time of when charging completes.
- [let scheduledStartTime: Date](./chargingtarget-swift.struct/scheduledstarttime.md)
  A scheduled time for when charging starts.
- [let estimatedRangeAtTarget: Measurement<UnitLength>?](./chargingtarget-swift.struct/estimatedrangeattarget.md)
  An estimated range of driving distance for the target state of charge.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting charging targets
- [let chargingTarget: ElectricVehicleStatusEvent.ChargingTarget?](./chargingtarget-swift.property.md)
  The desired target when charging an electric vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/chargingtarget-swift.struct)*