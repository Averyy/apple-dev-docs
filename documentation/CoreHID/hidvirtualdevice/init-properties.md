# init(properties:)

**Framework**: Core HID  
**Kind**: init

Creates a virtual HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init?(properties: HIDVirtualDevice.Properties)
```

#### Discussion

[`HIDVirtualDevice`](hidvirtualdevice.md) is created in an inactive state, notifications won’t be received and many functions won’t run until [`activate(delegate:)`](hidvirtualdevice/activate(delegate:).md) has run successfully.

## Parameters

- `properties`: The   for the virtual device. These values determine the device functionality.

## See Also

- [let deviceReference: HIDDeviceClient.DeviceReference](hidvirtualdevice/devicereference.md)
  The reference to the virtual HID device.
- [func activate(delegate: any HIDVirtualDeviceDelegate)](hidvirtualdevice/activate(delegate:).md)
  Activate a newly created virtual device to begin receiving notifications and enable functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/init(properties:))*