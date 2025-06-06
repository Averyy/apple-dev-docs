# CompleteInputReport

**Framework**: HIDDriverKit  
**Kind**: method

Processes the results of an asynchronous request for an input report.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void CompleteInputReport(OSAction * action, IOReturn status, uint32_t actualByteCount, uint64_t completionTimestamp);
```

#### Discussion

If an asynchronous request for an input report was successful, this method handles the report and schedules a new asynchronous request for an updated report. If the request was unsuccessful, this method retries the initial request, resetting the USB device as needed if it is unresponsive.

## Parameters

- `action`: The completion action.
- `status`: The completion status.
- `actualByteCount`: The number of bytes read.

## See Also

- [newReportDescriptor](iouserusbhosthiddevice/newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.
- [getReport](iouserusbhosthiddevice/getreport-6stqs.md)
  Gets a report from the HID device.
- [getReport](iouserusbhosthiddevice/getreport-2v8zk.md)
  Gets a report from the HID device.
- [setReport](iouserusbhosthiddevice/setreport.md)
  Sends a report to the HID device.
- [initInputReport](iouserusbhosthiddevice/initinputreport.md)
  Starts reading the input report from the device.
- [scheduleInputReportRetry](iouserusbhosthiddevice/scheduleinputreportretry.md)
  Retries a previous request for an input report.
- [cancelInputReportRetry](iouserusbhosthiddevice/cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.
- [TimerOccurred](iouserusbhosthiddevice/timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/completeinputreport)*