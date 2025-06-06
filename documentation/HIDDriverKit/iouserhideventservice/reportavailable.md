# ReportAvailable

**Framework**: HIDDriverKit  
**Kind**: method

Notifies the event service that an updated report is available from the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void ReportAvailable(uint64_t timestamp, uint32_t reportID, uint32_t reportLength, IOHIDReportType type, IOMemoryDescriptor * report, OSAction * action);
```

#### Discussion

Implement a custom version of this method in your event service. Use the [`TYPE`](https://developer.apple.com/documentation/DriverKit/TYPE) macro to let the system know that your method conforms to this prototype.

The system calls this method to notify your event service when a new report arrives.

## Parameters

- `timestamp`: The timestamp of the report.
- `reportID`: The unique ID associated with the report.
- `reportLength`: The length of the report in bytes.
- `type`: The report type.
- `report`: A memory descriptor that contains the raw data for the report.
- `action`: The   object that handles the asynchronous report callback.

## See Also

- [getElements](iouserhideventservice/getelements.md)
  Returns an array of elements that contain the parsed data from the HID device’s report.
- [handleReport](iouserhideventservice/handlereport.md)
  Converts an incoming device report into dispatchable events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/reportavailable)*