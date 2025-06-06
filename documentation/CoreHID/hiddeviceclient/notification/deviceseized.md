# HIDDeviceClient.Notification.deviceSeized

**Framework**: Core HID  
**Kind**: case

A notification that the device was seized by another client.

**Availability**:
- macOS 15.0+

## Declaration

```swift
case deviceSeized
```

#### Discussion

After the device is seized by another client, notifications are paused until [`HIDDeviceClient.Notification.deviceUnseized`](hiddeviceclient/notification/deviceunseized.md) is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/notification/deviceseized)*