# TwelvePtMovingWindowAverage

**Framework**: AudioDriverKit  
**Kind**: case

The 12-point moving window average filter algorithm.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
TwelvePtMovingWindowAverage
```

#### Discussion

Under this algorithm, the Host applies 12 point moving window average filter to the time stamps returned from [`GetCurrentZeroTimestamp`](iouseraudioclockdevice/getcurrentzerotimestamp.md).

## See Also

- [Raw](audiodriverkit/iouseraudioclockalgorithm/raw.md)
  An algorithm that uses timestamp values as-is.
- [SimpleIIR](audiodriverkit/iouseraudioclockalgorithm/simpleiir.md)
  The simple IIR filter algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclockalgorithm/twelveptmovingwindowaverage)*