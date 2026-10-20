# HIDDeviceManager

**Framework**: Core HID  
**Kind**: class  
**Role**: Class

A helper for discovering human interface devices (HID) connected to the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
actor HIDDeviceManager
```

## Mentions

- [Communicating with human interface devices](./communicatingwithhiddevices.md)

#### Overview

Use this class to specify matching criteria to filter all of the discoverable devices connected to the system into devices of interest. This is the main method of receiving a [`HIDDeviceClient.DeviceReference`](./hiddeviceclient/devicereference-swift.struct.md) used to create a [`HIDDeviceClient`](./hiddeviceclient.md).

Matching criteria are specified by creating [`HIDDeviceManager.DeviceMatchingCriteria`](./hiddevicemanager/devicematchingcriteria.md) and passing them to [`monitorNotifications(matchingCriteria:)`](./hiddevicemanager/monitornotifications%28matchingcriteria%29.md). References to devices that match the criteria are received using [`HIDDeviceManager.Notification.deviceMatched(_:)`](./hiddevicemanager/notification/devicematched%28_%29.md) notifications.

## Topics

### Create a device manager
- [init()](./hiddevicemanager/init%28%29.md)
  Creates a matching service for HID devices.
### Monitor device notifications
- [func monitorNotifications(matchingCriteria: [HIDDeviceManager.DeviceMatchingCriteria]) -> AsyncThrowingStream<HIDDeviceManager.Notification, any Error>](./hiddevicemanager/monitornotifications%28matchingcriteria%29.md)
  Creates an asynchronous stream that receives notifications for devices of interest.
- [HIDDeviceManager.Notification](./hiddevicemanager/notification.md)
  Notifications for HID devices.
### Structures
- [HIDDeviceManager.DeviceMatchingCriteria](./hiddevicemanager/devicematchingcriteria.md)
  Matching criteria used to filter HID devices.

## Relationships

### Conforms To
- [Actor](../Swift/actor.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Discovery
- [Discovering HID devices from Terminal](./discoveringhiddevicesfromterminal.md)
  Identify devices connected to your Mac from the command line.
- [HIDDeviceManager.DeviceMatchingCriteria](./hiddevicemanager/devicematchingcriteria.md)
  Matching criteria used to filter HID devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager)*