# handleReport

**Framework**: HIDDriverKit  
**Kind**: method

Handles an asynchronous report received from the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t handleReport(uint64_t timestamp, IOMemoryDescriptor * report, uint32_t reportLength, IOHIDReportType reportType, IOOptionBits options);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation of this method parses the report data and notifies attached interfaces of any changes.

## Parameters

- `report`: A memory descriptor that describes the report.
- `reportType`: The type of report.
- `options`: Options to specify in the request. No options are currently supported, and the default value is  .

## See Also

- [getReport](iohiddevice/getreport.md)
  Gets a report from the HID device.
- [setReport](iohiddevice/setreport.md)
  Sends a report to the HID device.
- [CompleteReport](iohiddevice/completereport.md)
  Completes all async requests made when getting or setting a report.
- [Report Options](report-options-enum.md)
  The enumerated report options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddevice/handlereport)*