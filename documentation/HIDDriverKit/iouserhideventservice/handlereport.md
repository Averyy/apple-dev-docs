# handleReport

**Framework**: HIDDriverKit  
**Kind**: method

Converts an incoming device report into dispatchable events.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void handleReport(uint64_t timestamp, uint8_t * report, uint32_t reportLength, IOHIDReportType type, uint32_t reportID);
```

#### Discussion

Implement a custom version of this method and use the [`TYPE`](https://developer.apple.com/documentation/DriverKit/TYPE) macro to let the system know that your method conforms to this prototype.

In your custom implementation of this method, use the report data to gather the information you need to dispatch an appropriate event to the system. To simplify the parsing of the report data, use the [`getElements`](iouserhideventservice/getelements.md) method to populate a set of [`IOHIDElement`](iohidelement.md) objects with data from the report. You can then iterate over the elements to collect the data you need. Compare the report ID of each element to the value in the `reportID` parameter to determine which elements contain updated data. Dispatch events to the system using the methods of the [`IOHIDEventService`](iohideventservice.md) class, some of which this class overrides.

## Parameters

- `timestamp`: The timestamp of the report.
- `report`: A pointer to the raw bytes of the report.
- `reportLength`: The number of bytes of data in the   parameter.
- `type`: The report type.
- `reportID`: The unique ID associated with the report. If a report element has new data, it contains this ID.

## See Also

- [getElements](iouserhideventservice/getelements.md)
  Returns an array of elements that contain the parsed data from the HID device’s report.
- [ReportAvailable](iouserhideventservice/reportavailable.md)
  Notifies the event service that an updated report is available from the HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserhideventservice/handlereport)*