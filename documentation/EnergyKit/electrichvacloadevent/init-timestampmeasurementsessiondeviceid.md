# init(timestamp:measurement:session:deviceID:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electric HVAC load event.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
init(timestamp: Date, measurement: ElectricHVACLoadEvent.ElectricalMeasurement, session: ElectricHVACLoadEvent.Session, deviceID: String)
```

#### Discussion

> **Note**: [`EnergyKitError.invalidLoadEvent`](energykiterror/invalidloadevent.md)

## Parameters

- `timestamp`: The timestamp for when the event occurred.
- `measurement`: The electricity consumption or generation of a device.
- `session`: The session information.
- `deviceID`: The device’s unique stable identifier.

## See Also

- [ElectricHVACLoadEvent.Session](electrichvacloadevent/session-swift.struct.md)
  A session that tracks the event.
- [ElectricHVACLoadEvent.ElectricalMeasurement](electrichvacloadevent/electricalmeasurement.md)
  A description of the electricity consumed by a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/init(timestamp:measurement:session:deviceid:))*