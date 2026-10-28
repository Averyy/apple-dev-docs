# init(deviceReference:)

**Framework**: Core HID  
**Kind**: init  
**Role**: Initializer

Creates a client for a HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init?(deviceReference: HIDDeviceClient.DeviceReference)
```

## Discussion

After creating a [`HIDDeviceClient`](../hiddeviceclient.md), notifications about the associated device arrive in [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](./monitornotifications%28reportidstomonitor,elementstomonitor%29.md).

## Parameters

- `deviceReference`: The reference to the target HID device that arrive using [`HIDDeviceManager`](../hiddevicemanager.md). For more details, see [`HIDDeviceClient.DeviceReference`](./devicereference-swift.struct.md).

## See Also

### Create a device client
- [HIDDeviceClient.DeviceReference](./devicereference-swift.struct.md)
  A reference to a HID device on the system.
- [let deviceReference: HIDDeviceClient.DeviceReference](./devicereference-swift.property.md)
  The reference to the HID device used to create the  HID client device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/init(devicereference:))*