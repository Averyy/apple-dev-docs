# HIDDeviceManager

**Framework**: Core HID  
**Kind**: class

A helper for discovering human interface devices (HID) connected to the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
actor HIDDeviceManager
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Overview

Use this class to specify matching criteria to filter all of the discoverable devices connected to the system into devices of interest. This is the main method of receiving a [`HIDDeviceClient.DeviceReference`](hiddeviceclient/devicereference-swift.struct.md) used to create a [`HIDDeviceClient`](hiddeviceclient.md).

Matching criteria are specified by creating [`HIDDeviceManager.DeviceMatchingCriteria`](hiddevicemanager/devicematchingcriteria.md) and passing them to [`monitorNotifications(matchingCriteria:)`](hiddevicemanager/monitornotifications(matchingcriteria:).md). References to devices that match the criteria are received using [`HIDDeviceManager.Notification.deviceMatched(_:)`](hiddevicemanager/notification/devicematched(_:).md) notifications.

## Topics

### Create a device manager
- [init()](hiddevicemanager/init.md)
  Creates a matching service for HID devices.
### Monitor device notifications
- [func monitorNotifications(matchingCriteria: [HIDDeviceManager.DeviceMatchingCriteria]) -> AsyncThrowingStream<HIDDeviceManager.Notification, any Error>](hiddevicemanager/monitornotifications(matchingcriteria:).md)
  Creates an asynchronous stream that receives notifications for devices of interest.
- [HIDDeviceManager.Notification](hiddevicemanager/notification.md)
  Notifications for HID devices.
### Structures
- [HIDDeviceManager.DeviceMatchingCriteria](hiddevicemanager/devicematchingcriteria.md)
  Matching criteria used to filter HID devices.
### Instance Properties
- [var unownedExecutor: UnownedSerialExecutor](hiddevicemanager/unownedexecutor.md)
  Retrieve the executor for this actor as an optimized, unowned reference.
### Default Implementations
- [Actor Implementations](hiddevicemanager/actor-implementations.md)
- [Equatable Implementations](hiddevicemanager/equatable-implementations.md)
- [Hashable Implementations](hiddevicemanager/hashable-implementations.md)

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Discovering HID devices from Terminal](discoveringhiddevicesfromterminal.md)
  Identify devices connected to your Mac from the command line.
- [HIDDeviceManager.DeviceMatchingCriteria](hiddevicemanager/devicematchingcriteria.md)
  Matching criteria used to filter HID devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager)*