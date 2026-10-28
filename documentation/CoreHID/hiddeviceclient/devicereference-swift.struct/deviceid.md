# deviceID

**Framework**: Core HID  
**Kind**: property  
**Role**: Instance Property

The unique ID for the associated HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let deviceID: UInt64
```

## Discussion

A [`HIDDeviceClient.DeviceReference`](../devicereference-swift.struct.md)with the same [`deviceID`](./deviceid.md) is an equivalent reference to the same device, and a [`deviceID`](./deviceid.md) for a device is equivalent across the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/devicereference-swift.struct/deviceid)*