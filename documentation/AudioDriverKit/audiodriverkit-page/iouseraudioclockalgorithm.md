# IOUserAudioClockAlgorithm

**Framework**: AudioDriverKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe clock-smoothing algorithms.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
enum IOUserAudioClockAlgorithm : uint32_t;
```

## Topics

### Clock-Smoothing Algorithms
- [Raw](./iouseraudioclockalgorithm/raw.md)
  An algorithm that uses timestamp values as-is.
- [SimpleIIR](./iouseraudioclockalgorithm/simpleiir.md)
  The simple IIR filter algorithm.
- [TwelvePtMovingWindowAverage](./iouseraudioclockalgorithm/twelveptmovingwindowaverage.md)
  The 12-point moving window average filter algorithm.

## See Also

### Working with Clock Device Behavior
- [SetClockAlgorithm](../iouseraudioclockdevice/setclockalgorithm.md)
  Sets the clock algorithm of the clock device.
- [GetClockAlgorithm](../iouseraudioclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [SetClockIsStable](../iouseraudioclockdevice/setclockisstable.md)
  Sets a Boolean value to represent the clock’s stability.
- [GetClockIsStable](../iouseraudioclockdevice/getclockisstable.md)
  Gets a Boolean value that represents the clock’s stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclockalgorithm)*