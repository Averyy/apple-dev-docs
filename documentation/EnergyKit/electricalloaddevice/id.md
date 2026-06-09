# id

**Framework**: EnergyKit  
**Kind**: property

A unique, stable identifier for a device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let id: String
```

#### Discussion

Provide this identifier when you create an [`ElectricalLoadDevice`](electricalloaddevice.md) instance for submitting electrical load events. The EnergyKit framework uses this identifier to associate events with devices and generate device-specific insights.

The system expects the value to be a maximum of 64 UTF-8 characters, such as a UUID. Ensure the identifier:

- Isn’t empty, and is less than or equal to 64 characters
- Uses only alphanumeric, space, hyphen, and apostrophe characters
- Starts and ends with an alphanumeric character

## See Also

- [let name: String](electricalloaddevice/name.md)
  A human-readable name for the device.
- [let type: ElectricalLoadDevice.DeviceType](electricalloaddevice/type.md)
  The type of electrical load device.
- [ElectricalLoadDevice.DeviceType](electricalloaddevice/devicetype.md)
  The type of electrical load device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricalloaddevice/id)*