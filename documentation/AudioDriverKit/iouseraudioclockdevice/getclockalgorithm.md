# GetClockAlgorithm

**Framework**: AudioDriverKit  
**Kind**: method

Gets the clock algorithm of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
IOUserAudioClockAlgorithm GetClockAlgorithm();
```

#### Return Value

The clock algorithm of the clock device.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetClockAlgorithm](iouseraudioclockdevice/setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [IOUserAudioClockAlgorithm](audiodriverkit/iouseraudioclockalgorithm.md)
  Values that describe clock-smoothing algorithms.
- [SetClockIsStable](iouseraudioclockdevice/setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.
- [GetClockIsStable](iouseraudioclockdevice/getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getclockalgorithm)*