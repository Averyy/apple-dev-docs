# HIDDeviceClient.Notification.deviceRemoved

**Framework**: Core HID  
**Kind**: case

A notification that the device is no longer connected to the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
case deviceRemoved
```

#### Discussion

After the device is removed, no other notifications occur and most methods fail. Discard the [`HIDDeviceClient`](hiddeviceclient.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/notification/deviceremoved)*