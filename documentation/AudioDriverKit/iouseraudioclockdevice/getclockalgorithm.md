# GetClockAlgorithm

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the clock algorithm of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
IOUserAudioClockAlgorithm GetClockAlgorithm();
```

## Return Value

The clock algorithm of the clock device.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Clock Device Behavior
- [SetClockAlgorithm](./setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](../audiodriverkit-page/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [SetClockIsStable](./setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.
- [GetClockIsStable](./getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getclockalgorithm)*