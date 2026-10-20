# TimerOccurred

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Handles timeout-related actions when retrying input report requests.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void TimerOccurred(OSAction *action, uint64_t time);
```

#### Discussion

Don’t call this method directly. When the service needs to retry an input request, it delays the start of that request by a short amount of time. This method processes that delay and begins the new request.

## Parameters

- `action`: The timer action.
- `time`: The time.

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
- [scheduleInputReportRetry](./scheduleinputreportretry.md)
  Retries a previous request for an input report.
- [cancelInputReportRetry](./cancelinputreportretry.md)
  Cancels a retry attempt for an input report request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/timeroccurred)*