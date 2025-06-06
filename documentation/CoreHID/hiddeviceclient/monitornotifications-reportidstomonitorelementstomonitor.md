# monitorNotifications(reportIDsToMonitor:elementsToMonitor:)

**Framework**: Corehid  
**Kind**: method

Creates an asynchronous that receives notifications about the associated device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func monitorNotifications(reportIDsToMonitor: [ClosedRange<HIDReportID>], elementsToMonitor: [HIDElement]) -> AsyncThrowingStream<HIDDeviceClient.Notification, any Error>
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Return Value

An asynchronous stream that receive notifications.

#### Discussion

Notifications come in asynchronously from the device at arbitrary times when relevant events occur.

Example usage:

```swift
for await notification in try await client.monitorNotifications(reportIDsToMonitor: [HIDReportID.allReports], elementsToMonitor: await client.elements) {
switch notification {
case .inputReport(let reportID, let report, let timestamp):
    break
case .elementUpdates(let values):
    break
case .deviceSeized:
    break
case .deviceUnseized:
    break
case .deviceRemoved:
    break
}
```

> **Note**: [`HIDDeviceError`](hiddeviceerror.md) if there is an issue with setup.

## Parameters

- `reportIDsToMonitor`: The report IDs that should trigger an   notification.
- `elementsToMonitor`: The elements that should trigger an   notification. Elements of interest can be parsed from  .

## See Also

- [HIDDeviceClient.Notification](hiddeviceclient/notification.md)
  Notifications for a HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/monitornotifications(reportidstomonitor:elementstomonitor:))*