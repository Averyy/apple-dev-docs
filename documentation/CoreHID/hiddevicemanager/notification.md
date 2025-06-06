# HIDDeviceManager.Notification

**Framework**: Core HID  
**Kind**: enum

Notifications for HID devices.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum Notification
```

#### Overview

You can receive these notifications using [`monitorNotifications(matchingCriteria:)`](hiddevicemanager/monitornotifications(matchingcriteria:).md).

## Topics

### Enumeration Cases
- [case deviceMatched(HIDDeviceClient.DeviceReference)](hiddevicemanager/notification/devicematched(_:).md)
  A notification that a device matched the device criteria.
- [case deviceRemoved(HIDDeviceClient.DeviceReference)](hiddevicemanager/notification/deviceremoved(_:).md)
  A notification that a previously matched device was removed from the system.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func monitorNotifications(matchingCriteria: [HIDDeviceManager.DeviceMatchingCriteria]) -> AsyncThrowingStream<HIDDeviceManager.Notification, any Error>](hiddevicemanager/monitornotifications(matchingcriteria:).md)
  Creates an asynchronous stream that receives notifications for devices of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/notification)*