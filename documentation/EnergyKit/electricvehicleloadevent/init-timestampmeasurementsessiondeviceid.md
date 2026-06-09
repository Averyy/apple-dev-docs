# init(timestamp:measurement:session:deviceID:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electric vehicle load event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
init(timestamp: Date, measurement: ElectricVehicleLoadEvent.ElectricalMeasurement, session: ElectricVehicleLoadEvent.Session, deviceID: String)
```

#### Discussion

> **Note**: [`EnergyKitError.invalidLoadEvent`](energykiterror/invalidloadevent.md)

## Parameters

- `timestamp`: The timestamp for when the event occurs.
- `measurement`: The electricity consumption or generation of a device.
- `session`: The session information.
- `deviceID`: The device’s unique stable identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/init(timestamp:measurement:session:deviceid:))*