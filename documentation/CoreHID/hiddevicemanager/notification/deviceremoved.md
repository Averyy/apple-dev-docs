# HIDDeviceManager.Notification.deviceRemoved(_:)

**Framework**: Core HID  
**Kind**: case

A notification that a previously matched device was removed from the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
case deviceRemoved(HIDDeviceClient.DeviceReference)
```

#### Discussion

Any created [`HIDDeviceClient`](hiddeviceclient.md) also receives a [`HIDDeviceClient.Notification.deviceRemoved`](hiddeviceclient/notification/deviceremoved.md) notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/notification/deviceremoved(_:))*