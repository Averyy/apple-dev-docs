# cancelInputReportRetry

**Framework**: HIDDriverKit  
**Kind**: method

Cancels a retry attempt for an input report request.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void cancelInputReportRetry();
```

#### Discussion

Don’t call this method directly. The [`CompleteInputReport`](iouserusbhosthiddevice/completeinputreport.md) method calls it automatically when a retry attempt succeeds.

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
- [CompleteInputReport](iouserusbhosthiddevice/completeinputreport.md)
  Processes the results of an asynchronous request for an input report.
- [scheduleInputReportRetry](iouserusbhosthiddevice/scheduleinputreportretry.md)
  Retries a previous request for an input report.
- [TimerOccurred](iouserusbhosthiddevice/timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/cancelinputreportretry)*