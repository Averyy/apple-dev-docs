# ReportAvailable

**Framework**: HIDDriverKit  
**Kind**: method

Notifies the interface that an updated report is available from the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void ReportAvailable(uint64_t timestamp, uint32_t reportID, uint32_t reportLength, IOHIDReportType type, IOMemoryDescriptor * report, OSAction * action);
```

#### Discussion

Implement a custom version of this method in the [`OSAction`](https://developer.apple.com/documentation/DriverKit/OSAction) object you use to open a session with the interface. Use the [`TYPE`](https://developer.apple.com/documentation/DriverKit/TYPE) macro to let the system know that your method conforms to this prototype.

Don’t call this method directly. The system calls your custom method when a new report arrives.

## Parameters

- `timestamp`: The timestamp of the report.
- `reportID`: The unique ID associated with the report.
- `reportLength`: The length of the report in bytes.
- `type`: The report type.
- `report`: A memory descriptor that contains the raw data for the report.
- `action`: The   object that handles the asynchronous report callback.

## See Also

- [AddReportToPool](iohidinterface/addreporttopool.md)
  Adds a memory descriptor to the report pool.
- [processReport](iohidinterface/processreport.md)
  Parses the contents of the specified report and updates the interface’s elements.
- [GetReport](iohidinterface/getreport.md)
  Retrieves a new input report from the HID device.
- [SetReport](iohidinterface/setreport.md)
  Sends a report to the HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/reportavailable)*