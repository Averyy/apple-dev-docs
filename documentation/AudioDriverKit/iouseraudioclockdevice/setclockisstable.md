# SetClockIsStable

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value to represent the clock’s stability.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetClockIsStable(bool in_clock_is_stable);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_clock_is_stable`: `true` if the clock is stable; otherwise, `false`.

## See Also

### Working with Clock Device Behavior
- [SetClockAlgorithm](./setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [GetClockAlgorithm](./getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](../audiodriverkit-page/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [GetClockIsStable](./getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/setclockisstable)*