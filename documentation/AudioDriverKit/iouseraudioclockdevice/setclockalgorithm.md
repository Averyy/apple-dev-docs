# SetClockAlgorithm

**Framework**: AudioDriverKit  
**Kind**: method

Sets the clock algorithm of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetClockAlgorithm(IOUserAudioClockAlgorithm in_clock_algorithm);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

Drivers can change the transport type of the clock device dynamically. If successful, changing the transport type sends a notification to the host to update the object state.

## Parameters

- `in_clock_algorithm`: The clock algorithm to set.

## See Also

- [GetClockAlgorithm](iouseraudioclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](audiodriverkit/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [SetClockIsStable](iouseraudioclockdevice/setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.
- [GetClockIsStable](iouseraudioclockdevice/getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setclockalgorithm)*