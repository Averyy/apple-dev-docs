# init(timestamp:measurement:session:device:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electric vehicle load event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(timestamp: Date, measurement: ElectricVehicleLoadEvent.ElectricalMeasurement, session: ElectricVehicleLoadEvent.Session, device: ElectricalLoadDevice)
```

#### Discussion

> **Note**:  [`EnergyKitError.invalidLoadEvent`](energykiterror/invalidloadevent.md)

## Parameters

- `timestamp`: The time when the event occurs.
- `measurement`: The electricity consumption or generation of the device.
- `session`: The session information.
- `device`: The identifier of the [`ElectricalLoadDevice`](electricalloaddevice.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/init(timestamp:measurement:session:device:))*