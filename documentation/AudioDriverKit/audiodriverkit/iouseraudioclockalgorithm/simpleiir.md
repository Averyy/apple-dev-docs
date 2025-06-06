# SimpleIIR

**Framework**: AudioDriverKit  
**Kind**: case

The simple IIR filter algorithm.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
SimpleIIR
```

#### Discussion

Under this algorithm, the Host applies a simple IIR filter to the time stamp stream. This is the default algorithm used for devices that don’t implement `DevicePropertyClockAlgorithm`.

## See Also

- [Raw](audiodriverkit/iouseraudioclockalgorithm/raw.md)
  An algorithm that uses timestamp values as-is.
- [TwelvePtMovingWindowAverage](audiodriverkit/iouseraudioclockalgorithm/twelveptmovingwindowaverage.md)
  The 12-point moving window average filter algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclockalgorithm/simpleiir)*