# getReport

**Framework**: HIDDriverKit  
**Kind**: method

Gets a report from the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t getReport(IOMemoryDescriptor * report, IOHIDReportType reportType, IOOptionBits options, uint32_t completionTimeout, OSAction * action);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The default implementation of this method does nothing. Subclasses must override it and use their implementation to retrieve the report information from the device.

## Parameters

- `report`: A memory descriptor that contains the report from the HID device.
- `reportType`: The report type.
- `options`: The lower 8 bits of the report ID. The other 24 bits are options to specify the request.
- `completionTimeout`: The amount of time, in milliseconds, after which to abort the command if the entire command hasn’t completed.
- `action`: The function to call when the request completes. If you omit this function, the method executes synchronously, blocking the current thread until the request completes.

## See Also

- [handleReport](iohiddevice/handlereport.md)
  Handles an asynchronous report received from the HID device.
- [setReport](iohiddevice/setreport.md)
  Sends a report to the HID device.
- [CompleteReport](iohiddevice/completereport.md)
  Completes all async requests made when getting or setting a report.
- [Report Options](report-options-enum.md)
  The enumerated report options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddevice/getreport)*