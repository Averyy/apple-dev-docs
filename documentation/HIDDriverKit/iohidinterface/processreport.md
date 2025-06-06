# processReport

**Framework**: HIDDriverKit  
**Kind**: method

Parses the contents of the specified report and updates the interface’s elements.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void processReport(uint64_t timestamp, uint8_t * report, uint32_t reportLength, IOHIDReportType type, uint32_t reportID);
```

#### Discussion

This method uses the provided report data to update the [`IOHIDElement`](iohidelement.md) objects associated with this interface. Upon receiving a new report, call this method before you call the [`getElements`](iohidinterface/getelements.md) method.

## Parameters

- `timestamp`: The timestamp of the report.
- `report`: A pointer to the bytes of the report.
- `reportLength`: The number of bytes in the   parameter.
- `type`: The report type.
- `reportID`: The unique ID associated with the report.

## See Also

- [ReportAvailable](iohidinterface/reportavailable.md)
  Notifies the interface that an updated report is available from the HID device.
- [AddReportToPool](iohidinterface/addreporttopool.md)
  Adds a memory descriptor to the report pool.
- [GetReport](iohidinterface/getreport.md)
  Retrieves a new input report from the HID device.
- [SetReport](iohidinterface/setreport.md)
  Sends a report to the HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/processreport)*