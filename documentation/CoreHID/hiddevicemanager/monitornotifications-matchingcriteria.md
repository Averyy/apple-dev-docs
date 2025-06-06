# monitorNotifications(matchingCriteria:)

**Framework**: Core HID  
**Kind**: method

Creates an asynchronous stream that receives notifications for devices of interest.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func monitorNotifications(matchingCriteria: [HIDDeviceManager.DeviceMatchingCriteria]) -> AsyncThrowingStream<HIDDeviceManager.Notification, any Error>
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Return Value

An asynchronous stream that receives notifications.

#### Discussion

Notifications come in asynchronously from the manager at arbitrary times when relevant events occur.

Example usage:

```swift
let searchCriteria = HIDDeviceManager.DeviceMatchingCriteria(primaryUsage: .genericDesktop(.keyboard), isBuiltIn: false)
for await notification in await manager.monitorNotifications(matchingCriteria: [searchCriteria]) {
    switch notification {
    case .deviceMatched(let deviceReference):
        client = HIDDeviceClient(deviceReference: deviceReference)
        break
    case .deviceRemoved(_):
        continue
    }
}
```

> **Note**: [`HIDDeviceError`](hiddeviceerror.md) if there is an issue with setup.

[`HIDDeviceError`](hiddeviceerror.md) if there is an issue with setup.

## Parameters

- `matchingCriteria`: A set of   for matching devices connected to the system. Criteria are considered separately, if one set is specified that matches one device, with a second set that matches five other devices, all six devices are matched. Matched devices result in a   notification. Matched devices are ready for connections using   until a   notification is received for the device.

## See Also

- [HIDDeviceManager.Notification](hiddevicemanager/notification.md)
  Notifications for HID devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddevicemanager/monitornotifications(matchingcriteria:))*