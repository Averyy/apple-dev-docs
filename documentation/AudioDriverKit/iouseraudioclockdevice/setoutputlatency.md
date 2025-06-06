# SetOutputLatency

**Framework**: AudioDriverKit  
**Kind**: method

Sets the output latency of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetOutputLatency(uint32_t in_latency);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Drivers can change the output latency of the clock device dynamically. If successful, changing the available output latency sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_latency`: The output latency value to set.

## See Also

- [GetSupportsPrewarming](iouseraudioclockdevice/getsupportsprewarming.md)
  Returns a Boolean value that indicates clock device’s support for prewarming.
- [SetZeroTimeStampPeriod](iouseraudioclockdevice/setzerotimestampperiod.md)
  Sets the zero time stamp of the clock device.
- [GetZeroTimestampPeriod](iouseraudioclockdevice/getzerotimestampperiod.md)
  Gets the zero time stamp of the clock device.
- [GetOutputLatency](iouseraudioclockdevice/getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](iouseraudioclockdevice/setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](iouseraudioclockdevice/getinputlatency.md)
  Get the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setoutputlatency)*