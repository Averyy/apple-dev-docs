# init(timestamp:device:venueID:status:stateOfCharge:energy:estimatedRange:chargingTarget:sessionIdentifier:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electric vehicle status event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(timestamp: Date, device: ElectricalLoadDevice, venueID: UUID, status: ElectricVehicleStatusEvent.Status, stateOfCharge: Int, energy: Measurement<UnitEnergy>, estimatedRange: Measurement<UnitLength>? = nil, chargingTarget: ElectricVehicleStatusEvent.ChargingTarget? = nil, sessionIdentifier: UUID? = nil)
```

## Parameters

- `timestamp`: The time when the status event occurs.
- `device`: The device identifier that [`ElectricalLoadDevice`](electricalloaddevice.md) creates.
- `venueID`: An identifier for the venue in which the event occurs.
- `status`: The current status of the vehicle relative to charger connection.
- `stateOfCharge`: The state of charge percentage (0-100) at the time of the event.
- `energy`: The state of charge in milliwatt-hours at the time of the event.
- `estimatedRange`: The estimated range based on current state, or `nil` if the range is unavailable.
- `chargingTarget`: The target information for the charging session, or `nil` if the information is unavailable.
- `sessionIdentifier`: An identifier for the [`ElectricVehicleLoadEvent`](electricvehicleloadevent.md) session, or `nil` if not applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/init(timestamp:device:venueid:status:stateofcharge:energy:estimatedrange:chargingtarget:sessionidentifier:))*