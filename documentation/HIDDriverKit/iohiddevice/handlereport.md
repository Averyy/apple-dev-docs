# handleReport

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Handles an asynchronous report received from the HID device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t handleReport(uint64_t timestamp, IOMemoryDescriptor *report, uint32_t reportLength, IOHIDReportType reportType, IOOptionBits options);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The default implementation of this method parses the report data and notifies attached interfaces of any changes.

## Parameters

- `report`: A memory descriptor that describes the report.
- `reportType`: The type of report.
- `options`: Options to specify in the request. No options are currently supported, and the default value is `0`.

## See Also

### Processing Device Reports
- [getReport](./getreport.md)
  Gets a report from the HID device.
- [setReport](./setreport.md)
  Sends a report to the HID device.
- [CompleteReport](./completereport.md)
  Completes all async requests made when getting or setting a report.
- [Report Options](../report-options-enum.md)
  The enumerated report options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddevice/handlereport)*