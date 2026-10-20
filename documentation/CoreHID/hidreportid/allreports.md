# allReports

**Framework**: Core HID  
**Kind**: property  
**Role**: Type Property

A convenient definition that represents every possible report ID.

**Availability**:
- macOS 15.0+

## Declaration

```swift
static let allReports: ClosedRange<HIDReportID>
```

#### Discussion

This can be useful when specifying the report IDs to monitor in [`monitorNotifications(reportIDsToMonitor:elementsToMonitor:)`](../hiddeviceclient/monitornotifications%28reportidstomonitor,elementstomonitor%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidreportid/allreports)*