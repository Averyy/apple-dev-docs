# deviceReference

**Framework**: Core HID  
**Kind**: property

The reference to the virtual HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
final let deviceReference: HIDDeviceClient.DeviceReference
```

#### Discussion

Use to create a [`HIDDeviceClient`](hiddeviceclient.md), if creating a device and monitoring it within the same app is desired. For more details, see [`HIDDeviceClient.DeviceReference`](hiddeviceclient/devicereference-swift.struct.md).

## See Also

- [init?(properties: HIDVirtualDevice.Properties)](hidvirtualdevice/init(properties:).md)
  Creates a virtual HID device.
- [func activate(delegate: any HIDVirtualDeviceDelegate)](hidvirtualdevice/activate(delegate:).md)
  Activate a newly created virtual device to begin receiving notifications and enable functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/devicereference)*