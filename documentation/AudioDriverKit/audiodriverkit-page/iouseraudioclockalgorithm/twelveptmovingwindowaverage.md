# TwelvePtMovingWindowAverage

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The 12-point moving window average filter algorithm.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
TwelvePtMovingWindowAverage
```

#### Discussion

Under this algorithm, the Host applies 12 point moving window average filter to the time stamps returned from [`GetCurrentZeroTimestamp`](../../iouseraudioclockdevice/getcurrentzerotimestamp.md).

## See Also

### Clock-Smoothing Algorithms
- [Raw](./raw.md)
  An algorithm that uses timestamp values as-is.
- [SimpleIIR](./simpleiir.md)
  The simple IIR filter algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclockalgorithm/twelveptmovingwindowaverage)*