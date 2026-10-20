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

## Parameters

- `report`: A memory descriptor that describes the report to send to the HID device.
- `reportType`: The report type.
- `options`: The lower 8 bits of the report ID. The other 24 bits are options to specify the request.
- `completionTimeout`: The amount of time, in milliseconds, after which to abort the command if the entire command hasn’t finished.
- `action`: The [`OSAction`](../../DriverKit/osaction.md) object to execute when the request completes. Specify `NULL` to execute the request synchronously, which blocks the current thread until the request completes.

## See Also

### Managing Device Reports
- [newReportDescriptor](./newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.
- [getReport](./getreport-6stqs.md)
  Gets a report from the HID device.
- [getReport](./getreport-2v8zk.md)
  Gets a report from the HID device.
- [initInputReport](./initinputreport.md)
  Starts reading the input report from the device.
- [CompleteInputReport](./completeinputreport.md)
  Processes the results of an asynchronous request for an input report.
- [scheduleInputReportRetry](./scheduleinputreportretry.md)
  Retries a previous request for an input report.
- [cancelInputReportRetry](./cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.
- [TimerOccurred](./timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/setreport)*