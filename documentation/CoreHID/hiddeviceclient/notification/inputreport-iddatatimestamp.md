# HIDDeviceClient.Notification.inputReport(id:data:timestamp:)

**Framework**: Core HID  
**Kind**: case

A notification that an input report was received from the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
case inputReport(id: HIDReportID?, data: Data, timestamp: SuspendingClock.Instant)
```

## Parameters

- `id`: The ID of the report. This may not be populated if the descriptor contains only one report.
- `data`: The raw bytes of the report. If there are multiple reports, the first byte is the report ID.
- `timestamp`: The time the report was received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hiddeviceclient/notification/inputreport(id:data:timestamp:))*