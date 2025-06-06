# SetClockIsStable

**Framework**: AudioDriverKit  
**Kind**: method

Sets a Boolean value to represent the clock’s stability.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetClockIsStable(bool in_clock_is_stable);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_clock_is_stable`:   if the clock is stable; otherwise,  .

## See Also

- [SetClockAlgorithm](iouseraudioclockdevice/setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [GetClockAlgorithm](iouseraudioclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](audiodriverkit/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [GetClockIsStable](iouseraudioclockdevice/getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setclockisstable)*