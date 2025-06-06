# IOUserAudioClockAlgorithm

**Framework**: AudioDriverKit  
**Kind**: enum

Values that describe clock-smoothing algorithms.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioClockAlgorithm : uint32_t;
```

## Topics

### Clock-Smoothing Algorithms
- [Raw](audiodriverkit/iouseraudioclockalgorithm/raw.md)
  An algorithm that uses timestamp values as-is.
- [SimpleIIR](audiodriverkit/iouseraudioclockalgorithm/simpleiir.md)
  The simple IIR filter algorithm.
- [TwelvePtMovingWindowAverage](audiodriverkit/iouseraudioclockalgorithm/twelveptmovingwindowaverage.md)
  The 12-point moving window average filter algorithm.

## See Also

- [SetClockAlgorithm](iouseraudioclockdevice/setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [GetClockAlgorithm](iouseraudioclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [SetClockIsStable](iouseraudioclockdevice/setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.
- [GetClockIsStable](iouseraudioclockdevice/getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclockalgorithm)*