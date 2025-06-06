# newReportDescriptor

**Framework**: HIDDriverKit  
**Kind**: method

Returns the data in the HID device’s report descriptor.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
OSData * newReportDescriptor();
```

#### Return Value

An [`OSData`](https://developer.apple.com/documentation/DriverKit/OSData) object containing the report descriptor for the device.

#### Discussion

The default implementation of this method fetches the report descriptor from the USB device and packages the resulting data into an [`OSData`](https://developer.apple.com/documentation/DriverKit/OSData) object.

## See Also

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
- [cancelInputReportRetry](iouserusbhosthiddevice/cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.
- [TimerOccurred](iouserusbhosthiddevice/timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/newreportdescriptor)*