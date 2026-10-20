# SimpleIIR

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The simple IIR filter algorithm.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
SimpleIIR
```

#### Discussion

Under this algorithm, the Host applies a simple IIR filter to the time stamp stream. This is the default algorithm used for devices that don’t implement `DevicePropertyClockAlgorithm`.

## See Also

### Clock-Smoothing Algorithms
- [Raw](./raw.md)
  An algorithm that uses timestamp values as-is.
- [TwelvePtMovingWindowAverage](./twelveptmovingwindowaverage.md)
  The 12-point moving window average filter algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclockalgorithm/simpleiir)*