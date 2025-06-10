# HIDDeviceClient.Notification

**Framework**: Core HID  
**Kind**: enum

Notifications for a HID device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
enum Notification
```

#### Overview

You can receive these notifications using [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md).

## Topics

### Enumeration Cases
- [HIDDeviceClient.Notification.deviceRemoved](hiddeviceclient/notification/deviceremoved.md)
  A notification that the device is no longer connected to the system.
- [HIDDeviceClient.Notification.deviceSeized](hiddeviceclient/notification/deviceseized.md)
  A notification that the device was seized by another client.
- [HIDDeviceClient.Notification.deviceUnseized](hiddeviceclient/notification/deviceunseized.md)
  A notification that the device is no longer seized.
- [HIDDeviceClient.Notification.elementUpdates(values:)](hiddeviceclient/notification/elementupdates(values:).md)
  A notification that elements of the device were updated.
- [case inputReport(id: HIDReportID?, data: Data, timestamp: SuspendingClock.Instant)](hiddeviceclient/notification/inputreport(id:data:timestamp:).md)
  A notification that an input report was received from the device.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func monitorNotifications(reportIDsToMonitor: [ClosedRange<HIDReportID>], elementsToMonitor: [HIDElement]) -> AsyncThrowingStream<HIDDeviceClient.Notification, any Error>](hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:).md)
  Creates an asynchronous that receives notifications about the associated device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/notification)*