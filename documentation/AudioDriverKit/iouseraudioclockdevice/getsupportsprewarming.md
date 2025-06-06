# GetSupportsPrewarming

**Framework**: AudioDriverKit  
**Kind**: method

Returns a Boolean value that indicates clock device’s support for prewarming.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool GetSupportsPrewarming();
```

#### Return Value

`true` if the clock device supports prewarming; `false` otherwise.

#### Discussion

A device that supports prewarming can enable a minimal state that allows it to be ready to start audio I/O immediately on demand.

This method synchronizes by using the work queue created by the object.

## See Also

- [SetZeroTimeStampPeriod](iouseraudioclockdevice/setzerotimestampperiod.md)
  Sets the zero time stamp of the clock device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getsupportsprewarming)*