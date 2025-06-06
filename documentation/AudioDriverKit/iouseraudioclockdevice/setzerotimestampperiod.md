# SetZeroTimeStampPeriod

**Framework**: AudioDriverKit  
**Kind**: method

Sets the zero time stamp of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetZeroTimeStampPeriod(uint32_t in_zts_period);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The parameter indicates the number of sample frames the host can expect between successive timestamps returned from [`GetCurrentZeroTimestamp`](iouseraudioclockdevice/getcurrentzerotimestamp.md). In other words, if [`GetCurrentZeroTimestamp`](iouseraudioclockdevice/getcurrentzerotimestamp.md) returns a sample time of `x`, the host can expect that the next valid timestamp it recieves will be `x + in_zero_timestamp_period`.

Only set this value during the [`PerformDeviceConfigurationChange`](iouseraudioclockdevice/performdeviceconfigurationchange.md) call. If you need to change the value at any other time, call [`RequestDeviceConfigurationChange`](iouseraudioclockdevice/requestdeviceconfigurationchange.md). This allows I/O to stop and calls [`PerformDeviceConfigurationChange`](iouseraudioclockdevice/performdeviceconfigurationchange.md), during which you can set the value.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_zts_period`: The zero time stamp period.

## See Also

- [GetSupportsPrewarming](iouseraudioclockdevice/getsupportsprewarming.md)
  Returns a Boolean value that indicates clock device’s support for prewarming.
- [GetZeroTimestampPeriod](iouseraudioclockdevice/getzerotimestampperiod.md)
  Gets the zero time stamp of the clock device.
- [SetOutputLatency](iouseraudioclockdevice/setoutputlatency.md)
  Sets the output latency of the clock device.
- [GetOutputLatency](iouseraudioclockdevice/getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](iouseraudioclockdevice/setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](iouseraudioclockdevice/getinputlatency.md)
  Get the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setzerotimestampperiod)*