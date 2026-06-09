# ElectricVehicleStatusEvent.Status.chargingIdle(_:)

**Framework**: EnergyKit  
**Kind**: case

A status that indicates the charger is connected but the vehicle isn’t charging.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
case chargingIdle(ElectricVehicleChargingReason.IdleReason)
```

## Mentions

- [Providing charging history for electric vehicles](providing-informative-charging-history-for-electric-vehicles.md)

#### Discussion

The associated [`ElectricVehicleChargingReason.IdleReason`](electricvehiclechargingreason/idlereason.md) explains why charging isn’t active.

## See Also

- [case chargingActive(ElectricVehicleChargingReason.ActiveReason)](electricvehiclestatusevent/status-swift.enum/chargingactive(_:).md)
  A status that indicates that the vehicle is actively charging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/status-swift.enum/chargingidle(_:))*