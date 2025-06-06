# GetClockIsStable

**Framework**: AudioDriverKit  
**Kind**: method

Gets a Boolean value that represents the clock’s stability.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool GetClockIsStable();
```

#### Return Value

`true` if the clock is stable; `false` otherwise.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetClockAlgorithm](iouseraudioclockdevice/setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [GetClockAlgorithm](iouseraudioclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](audiodriverkit/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [SetClockIsStable](iouseraudioclockdevice/setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getclockisstable)*