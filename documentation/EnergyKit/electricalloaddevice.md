# ElectricalLoadDevice

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

A type that identifies an electrical load device for event submission.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
struct ElectricalLoadDevice
```

## Mentions

- [Providing charging history for electric vehicles](./providing-informative-charging-history-for-electric-vehicles.md)

#### Overview

This structure represents the device tied to load events you submit. The device’s [`type`](./electricalloaddevice/type.md) can be an electric vehicle or an HVAC device.

For an example that uses an electrical load device, see [Optimizing home electricity usage](./optimizing-home-electricity-usage.md).

## Topics

### Creating a device identifier
- [init(id: String, name: String, type: ElectricalLoadDevice.DeviceType)](./electricalloaddevice/init%28id,name,type%29.md)
  Initializes an electrical load device identifier.
### Getting device information
- [let id: String](./electricalloaddevice/id.md)
  A unique, stable identifier for a device.
- [let name: String](./electricalloaddevice/name.md)
  A human-readable name for the device.
- [let type: ElectricalLoadDevice.DeviceType](./electricalloaddevice/type.md)
  The type of electrical load device.
- [ElectricalLoadDevice.DeviceType](./electricalloaddevice/devicetype.md)
  The type of electrical load device.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Device identification
- [protocol ElectricalLoadEventProtocol](./electricalloadeventprotocol.md)
  A type that can represent an electrical load event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricalloaddevice)*