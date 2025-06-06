# SetReport

**Framework**: HIDDriverKit  
**Kind**: method

Sends a report to the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t SetReport(IOMemoryDescriptor * report, IOHIDReportType reportType, uint32_t reportID, IOOptionBits options);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method sets the report by calling the [`setReport`](iohiddevice/setreport.md) method of its associated [`IOHIDDevice`](iohiddevice.md) object. When sending the report to the device, this method combines the `reportID` and `options` together, with the `reportID` occupying the lower 8 bits of a 32-bit integer, and the `options` occupying the upper 24 bits.

## Parameters

- `report`: A memory descriptor that contains the report data that you want to send to the HID device.
- `reportType`: The type of report you want to send to the device.
- `reportID`: The unique identifier for the report.
- `options`: Options to specify when sending the report.

## See Also

- [ReportAvailable](iohidinterface/reportavailable.md)
  Notifies the interface that an updated report is available from the HID device.
- [AddReportToPool](iohidinterface/addreporttopool.md)
  Adds a memory descriptor to the report pool.
- [processReport](iohidinterface/processreport.md)
  Parses the contents of the specified report and updates the interface’s elements.
- [GetReport](iohidinterface/getreport.md)
  Retrieves a new input report from the HID device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/setreport)*