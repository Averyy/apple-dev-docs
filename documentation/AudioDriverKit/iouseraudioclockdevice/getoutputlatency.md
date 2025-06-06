# GetOutputLatency

**Framework**: AudioDriverKit  
**Kind**: method

Gets the output latency of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
uint32_t GetOutputLatency();
```

#### Return Value

The output latency of the clock device.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [GetSupportsPrewarming](iouseraudioclockdevice/getsupportsprewarming.md)
  Returns a Boolean value that indicates clock device’s support for prewarming.
- [SetZeroTimeStampPeriod](iouseraudioclockdevice/setzerotimestampperiod.md)
  Sets the zero time stamp of the clock device.
- [GetZeroTimestampPeriod](iouseraudioclockdevice/getzerotimestampperiod.md)
  Gets the zero time stamp of the clock device.
- [SetOutputLatency](iouseraudioclockdevice/setoutputlatency.md)
  Sets the output latency of the clock device.
- [SetInputLatency](iouseraudioclockdevice/setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](iouseraudioclockdevice/getinputlatency.md)
  Get the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getoutputlatency)*