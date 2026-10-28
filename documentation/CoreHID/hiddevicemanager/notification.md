# HIDDeviceManager.Notification

**Framework**: Core HID  
**Kind**: enum  
**Role**: Enumeration

Notifications for HID devices.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum Notification
```

## Overview

You can receive these notifications using [`monitorNotifications(matchingCriteria:)`](./monitornotifications%28matchingcriteria%29.md).

## Topics

### Enumeration Cases
- [case deviceMatched(HIDDeviceClient.DeviceReference)](./notification/devicematched%28_%29.md)
  A notification that a device matched the device criteria.
- [case deviceRemoved(HIDDeviceClient.DeviceReference)](./notification/deviceremoved%28_%29.md)
  A notification that a previously matched device was removed from the system.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitor device notifications
- [func monitorNotifications(matchingCriteria: [HIDDeviceManager.DeviceMatchingCriteria]) -> AsyncThrowingStream<HIDDeviceManager.Notification, any Error>](./monitornotifications%28matchingcriteria%29.md)
  Creates an asynchronous stream that receives notifications for devices of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/notification)*