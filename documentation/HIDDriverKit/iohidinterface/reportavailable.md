# ReportAvailable

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Notifies the interface that an updated report is available from the HID device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void ReportAvailable(uint64_t timestamp, uint32_t reportID, uint32_t reportLength, IOHIDReportType type, IOMemoryDescriptor *report, OSAction *action);
```

#### Discussion

Implement a custom version of this method in the [`OSAction`](../../DriverKit/osaction.md) object you use to open a session with the interface. Use the [`TYPE`](../../DriverKit/type.md) macro to let the system know that your method conforms to this prototype.

Don’t call this method directly. The system calls your custom method when a new report arrives.

## Parameters

- `timestamp`: The timestamp of the report.
- `reportID`: The unique ID associated with the report.
- `reportLength`: The length of the report in bytes.
- `type`: The report type.
- `report`: A memory descriptor that contains the raw data for the report.
- `action`: The `OSAction` object that handles the asynchronous report callback.

## See Also

### Getting and Setting Input Reports
- [AddReportToPool](./addreporttopool.md)
  Adds a memory descriptor to the report pool.
- [processReport](./processreport.md)
  Parses the contents of the specified report and updates the interface’s elements.
- [GetReport](./getreport.md)
  Retrieves a new input report from the HID device.
- [SetReport](./setreport.md)
  Sends a report to the HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/reportavailable)*