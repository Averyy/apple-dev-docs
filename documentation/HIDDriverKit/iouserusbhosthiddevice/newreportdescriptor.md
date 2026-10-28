# newReportDescriptor

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the data in the HID device’s report descriptor.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual OSData * newReportDescriptor();
```

## Return Value

An [`OSData`](../../DriverKit/osdata.md) object containing the report descriptor for the device.

## Discussion

The default implementation of this method fetches the report descriptor from the USB device and packages the resulting data into an [`OSData`](../../DriverKit/osdata.md) object.

## See Also

### Managing Device Reports
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
- [TimerOccurred](./timeroccurred.md)
  Handles timeout-related actions when retrying input report requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/newreportdescriptor)*