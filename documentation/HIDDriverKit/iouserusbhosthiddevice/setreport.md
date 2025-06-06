# setReport

**Framework**: HIDDriverKit  
**Kind**: method

Sends a report to the HID device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t setReport(IOMemoryDescriptor * report, IOHIDReportType reportType, IOOptionBits options, uint32_t completionTimeout, OSAction * action);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `report`: A memory descriptor that describes the report to send to the HID device.
- `reportType`: The report type.
- `options`: The lower 8 bits of the report ID. The other 24 bits are options to specify the request.
- `completionTimeout`: The amount of time, in milliseconds, after which to abort the command if the entire command hasn’t finished.
- `action`: The   object to execute when the request completes. Specify   to execute the request synchronously, which blocks the current thread until the request completes.

## See Also

- [newReportDescriptor](iouserusbhosthiddevice/newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.
- [getReport](iouserusbhosthiddevice/getreport-6stqs.md)
  Gets a report from the HID device.
- [getReport](iouserusbhosthiddevice/getreport-2v8zk.md)
  Gets a report from the HID device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/setreport)*