# scheduleInputReportRetry

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Retries a previous request for an input report.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void scheduleInputReportRetry(kern_return_t reason);
```

## Discussion

Don’t call this method directly. The [`CompleteInputReport`](./completeinputreport.md) method calls it automatically to retry the previous request for the input report.

## Parameters

- `reason`: The reason the previous request failed.

## See Also

### Managing Device Reports
- [newReportDescriptor](./newreportdescriptor.md)
  Returns the data in the HID device’s report descriptor.
- [getReport](./getreport-6stqs.md)
  Gets a report from the HID device.
- [getReport](./getreport-2v8zk.md)
  Gets a report from the HID device.
- [setReport](./setreport.md)
  Sends a report to the HID device.
- [initInputReport](./initinputreport.md)
  Starts reading the input report from the device.
- [CompleteInputReport](./completeinputreport.md)
  Processes the results of an asynchronous request for an input report.
- [cancelInputReportRetry](./cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.
- [TimerOccurred](./timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/scheduleinputreportretry)*