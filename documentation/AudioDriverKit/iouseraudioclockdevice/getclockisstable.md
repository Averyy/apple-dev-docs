# GetClockIsStable

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets a Boolean value that represents the clock’s stability.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
bool GetClockIsStable();
```

## Return Value

`true` if the clock is stable; `false` otherwise.

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Clock Device Behavior
- [SetClockAlgorithm](./setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [GetClockAlgorithm](./getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](../audiodriverkit-page/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [SetClockIsStable](./setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getclockisstable)*