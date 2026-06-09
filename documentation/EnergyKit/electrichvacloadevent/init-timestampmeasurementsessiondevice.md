# init(timestamp:measurement:session:device:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electric HVAC load event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(timestamp: Date, measurement: ElectricHVACLoadEvent.ElectricalMeasurement, session: ElectricHVACLoadEvent.Session, device: ElectricalLoadDevice)
```

#### Discussion

> **Note**:  [`EnergyKitError.invalidLoadEvent`](energykiterror/invalidloadevent.md)

## Parameters

- `timestamp`: The time when the event occurs.
- `measurement`: The electricity consumption of the device.
- `session`: The session information.
- `device`: The device identifier created with [`ElectricalLoadDevice`](electricalloaddevice.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/init(timestamp:measurement:session:device:))*