# HIDDeviceClient.DeviceReference

**Framework**: Core HID  
**Kind**: struct  
**Role**: Structure

A reference to a HID device on the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct DeviceReference
```

#### Overview

A device reference exists for every discovered device. Use it to create an [`HIDDeviceClient`](../hiddeviceclient.md), and maintain the reference until someone removes the device.

## Topics

### Instance Properties
- [let deviceID: UInt64](./devicereference-swift.struct/deviceid.md)
  The unique ID for the associated HID device.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Create a device client
- [init?(deviceReference: HIDDeviceClient.DeviceReference)](./init%28devicereference%29.md)
  Creates a client for a HID device.
- [let deviceReference: HIDDeviceClient.DeviceReference](./devicereference-swift.property.md)
  The reference to the HID device used to create the  HID client device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/devicereference-swift.struct)*