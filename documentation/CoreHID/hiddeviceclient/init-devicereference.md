# init(deviceReference:)

**Framework**: Core HID  
**Kind**: init

Creates a client for a HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init?(deviceReference: HIDDeviceClient.DeviceReference)
```

#### Discussion

After creating a [`HIDDeviceClient`](hiddeviceclient.md), notifications about the associated device arrive in [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md).

## Parameters

- `deviceReference`: The reference to the target HID device that arrive using  . For more details, see  .

## See Also

- [HIDDeviceClient.DeviceReference](hiddeviceclient/devicereference-swift.struct.md)
  A reference to a HID device on the system.
- [let deviceReference: HIDDeviceClient.DeviceReference](hiddeviceclient/devicereference-swift.property.md)
  The reference to the HID device used to create the  HID client device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/init(devicereference:))*