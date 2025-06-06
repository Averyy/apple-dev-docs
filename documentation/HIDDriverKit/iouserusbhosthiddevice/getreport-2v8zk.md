# getReport

**Framework**: HIDDriverKit  
**Kind**: method

Gets a report from the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t getReport(IOMemoryDescriptor * report, IOHIDReportType reportType, IOOptionBits options, uint32_t completionTimeout, uint32_t * bytesTransferred);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The report read from the HID device.

## Parameters

- `report`: The report type.
- `reportType`: The lower 8 bits will represent the Report ID.  The other 24 bits are options to specify the request.
- `options`: Specifies an amount of time (in ms) after which the command will be aborted if the entire command has not been completed.

## See Also

- [newReportDescriptor](iouserusbhosthiddevice/newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.
- [getReport](iouserusbhosthiddevice/getreport-6stqs.md)
  Gets a report from the HID device.
- [setReport](iouserusbhosthiddevice/setreport.md)
  Sends a report to the HID device.
- [initInputReport](iouserusbhosthiddevice/initinputreport.md)
  Starts reading the input report from the device.
- [CompleteInputReport](iouserusbhosthiddevice/completeinputreport.md)
  Processes the results of an asynchronous request for an input report.
- [scheduleInputReportRetry](iouserusbhosthiddevice/scheduleinputreportretry.md)
  Retries a previous request for an input report.
- [cancelInputReportRetry](iouserusbhosthiddevice/cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.
- [TimerOccurred](iouserusbhosthiddevice/timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/getreport-2v8zk)*