# GetZeroTimestampPeriod

**Framework**: AudioDriverKit  
**Kind**: method

Gets the zero time stamp of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t GetZeroTimestampPeriod();
```

#### Return Value

The zero time stamp of the clock device.

#### Discussion

The return value indicates the number of sample frames the host can expect between successive timestamps returned from [`GetCurrentZeroTimestamp`](iouseraudioclockdevice/getcurrentzerotimestamp.md). In other words, if [`GetCurrentZeroTimestamp`](iouseraudioclockdevice/getcurrentzerotimestamp.md) returns a sample time of `x`, the host can expect that the next valid timestamp it recieves will be `x +` [`GetZeroTimestampPeriod`](iouseraudioclockdevice/getzerotimestampperiod.md).

This method synchronizes by using the work queue created by the object.

## See Also

- [GetSupportsPrewarming](iouseraudioclockdevice/getsupportsprewarming.md)
  Returns a Boolean value that indicates clock device’s support for prewarming.
- [SetZeroTimeStampPeriod](iouseraudioclockdevice/setzerotimestampperiod.md)
  Sets the zero time stamp of the clock device.
- [SetOutputLatency](iouseraudioclockdevice/setoutputlatency.md)
  Sets the output latency of the clock device.
- [GetOutputLatency](iouseraudioclockdevice/getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](iouseraudioclockdevice/setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](iouseraudioclockdevice/getinputlatency.md)
  Get the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getzerotimestampperiod)*