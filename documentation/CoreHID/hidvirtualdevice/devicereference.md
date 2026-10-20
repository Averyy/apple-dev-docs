# deviceReference

**Framework**: Core HID  
**Kind**: property  
**Role**: Instance Property

The reference to the virtual HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
final let deviceReference: HIDDeviceClient.DeviceReference
```

#### Discussion

Use to create a [`HIDDeviceClient`](../hiddeviceclient.md), if creating a device and monitoring it within the same app is desired. For more details, see [`HIDDeviceClient.DeviceReference`](../hiddeviceclient/devicereference-swift.struct.md).

## See Also

### Create a HID virtual device
- [init?(properties: HIDVirtualDevice.Properties)](./init%28properties%29.md)
  Creates a virtual HID device.
- [func activate(delegate: any HIDVirtualDeviceDelegate)](./activate%28delegate%29.md)
  Activate a newly created virtual device to begin receiving notifications and enable functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidvirtualdevice/devicereference)*