# setReport

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Sends a report to the HID device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t setReport(IOMemoryDescriptor *report, IOHIDReportType reportType, IOOptionBits options, uint32_t completionTimeout, OSAction *action);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The default implementation of this method does nothing. Subclasses must override it and use their implementation to send the report information to the device.

## Parameters

- `report`: A memory descriptor that describes the report to send to the HID device.
- `reportType`: The report type.
- `options`: The lower 8 bits of the report ID. The other 24 bits are options to specify the request.
- `completionTimeout`: The amount of time, in milliseconds, after which to abort the command if the entire command hasn’t finished.
- `action`: The [`OSAction`](../../DriverKit/osaction.md) object to execute when the request completes. Specify `NULL` to execute the request synchronously, which blocks the current thread until the request completes.

## See Also

### Processing Device Reports
- [handleReport](./handlereport.md)
  Handles an asynchronous report received from the HID device.
- [getReport](./getreport.md)
  Gets a report from the HID device.
- [CompleteReport](./completereport.md)
  Completes all async requests made when getting or setting a report.
- [Report Options](../report-options-enum.md)
  The enumerated report options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohiddevice/setreport)*