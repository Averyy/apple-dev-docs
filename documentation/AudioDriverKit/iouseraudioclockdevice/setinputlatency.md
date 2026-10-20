# SetInputLatency

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the input latency of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetInputLatency(uint32_t in_latency);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Drivers can change the input latency of the clock device dynamically. If successful, changing the available input latency sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_latency`: The input latency value to set.

## See Also

### Working with Timing and Latency
- [GetSupportsPrewarming](./getsupportsprewarming.md)
  Returns a Boolean value that indicates clock device’s support for prewarming.
- [SetZeroTimeStampPeriod](./setzerotimestampperiod.md)
  Sets the zero time stamp of the clock device.
- [GetZeroTimestampPeriod](./getzerotimestampperiod.md)
  Gets the zero time stamp of the clock device.
- [SetOutputLatency](./setoutputlatency.md)
  Sets the output latency of the clock device.
- [GetOutputLatency](./getoutputlatency.md)
  Gets the output latency of the clock device.
- [GetInputLatency](./getinputlatency.md)
  Get the input latency of the clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setinputlatency)*