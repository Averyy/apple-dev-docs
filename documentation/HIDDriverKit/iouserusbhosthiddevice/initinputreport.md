# initInputReport

**Framework**: HIDDriverKit  
**Kind**: method

Starts reading the input report from the device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t initInputReport();
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method requests the input report from the USB device asynchronously, delivering the results to the [`CompleteInputReport`](iouserusbhosthiddevice/completeinputreport.md) method.

You don’t need to call this method directly. The service’s [`Start`](iouserusbhosthiddevice/start.md) method calls it when the service first runs, and the service requests new input reports regularly.

## See Also

- [newReportDescriptor](iouserusbhosthiddevice/newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.
- [getReport](iouserusbhosthiddevice/getreport-6stqs.md)
  Gets a report from the HID device.
- [getReport](iouserusbhosthiddevice/getreport-2v8zk.md)
  Gets a report from the HID device.
- [setReport](iouserusbhosthiddevice/setreport.md)
  Sends a report to the HID device.
- [CompleteInputReport](iouserusbhosthiddevice/completeinputreport.md)
  Processes the results of an asynchronous request for an input report.
- [scheduleInputReportRetry](iouserusbhosthiddevice/scheduleinputreportretry.md)
  Retries a previous request for an input report.
- [cancelInputReportRetry](iouserusbhosthiddevice/cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.
- [TimerOccurred](iouserusbhosthiddevice/timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/initinputreport)*