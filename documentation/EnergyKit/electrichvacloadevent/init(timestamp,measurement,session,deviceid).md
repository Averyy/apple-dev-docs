# init(timestamp:measurement:session:deviceID:)

**Framework**: EnergyKit  
**Kind**: init  
**Role**: Initializer

Creates an electric HVAC load event.

**Availability**:
- iOS 26.0+ - Deprecated in 27.0
- iPadOS 26.0+ - Deprecated in 27.0
- Mac Catalyst

> **Deprecated**: Use init(timestamp:measurement:session:device:) instead

## Declaration

```swift
init(timestamp: Date, measurement: ElectricHVACLoadEvent.ElectricalMeasurement, session: ElectricHVACLoadEvent.Session, deviceID: String)
```

## Discussion

> **Throws**: [`EnergyKitError.invalidLoadEvent`](../energykiterror/invalidloadevent.md)

## Parameters

- `timestamp`: The timestamp for when the event occurs.
- `measurement`: The electricity consumption or generation of a device.
- `session`: The session information.
- `deviceID`: The device’s unique stable identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/init(timestamp:measurement:session:deviceid:))*