# HIDDeviceClient.Notification

**Framework**: Core HID  
**Kind**: enum  
**Role**: Enumeration

Notifications for a HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum Notification
```

## Overview

You can receive these notifications using [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](./monitornotifications%28reportidstomonitor,elementstomonitor%29.md).

## Topics

### Enumeration Cases
- [HIDDeviceClient.Notification.deviceRemoved](./notification/deviceremoved.md)
  A notification that the device is no longer connected to the system.
- [HIDDeviceClient.Notification.deviceSeized](./notification/deviceseized.md)
  A notification that the device was seized by another client.
- [HIDDeviceClient.Notification.deviceUnseized](./notification/deviceunseized.md)
  A notification that the device is no longer seized.
- [HIDDeviceClient.Notification.elementUpdates(values:)](./notification/elementupdates%28values%29.md)
  A notification that elements of the device were updated.
- [case inputReport(id: HIDReportID?, data: Data, timestamp: SuspendingClock.Instant)](./notification/inputreport%28id,data,timestamp%29.md)
  A notification that an input report was received from the device.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitor device notifications
- [func monitorNotifications(reportIDsToMonitor: [ClosedRange<HIDReportID>], elementsToMonitor: [HIDElement]) -> AsyncThrowingStream<HIDDeviceClient.Notification, any Error>](./monitornotifications%28reportidstomonitor,elementstomonitor%29.md)
  Creates an asynchronous that receives notifications about the associated device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/notification)*