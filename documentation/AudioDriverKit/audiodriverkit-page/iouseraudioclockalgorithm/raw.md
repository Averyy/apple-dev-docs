# Raw

**Framework**: AudioDriverKit  
**Kind**: case  
**Role**: Enumeration Case

An algorithm that uses timestamp values as-is.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
Raw
```

## Discussion

Under this algorithm, the Host doesn’t apply any filtering to the time stamps returned from [`GetCurrentZeroTimestamp`](../../iouseraudioclockdevice/getcurrentzerotimestamp.md).

## See Also

### Clock-Smoothing Algorithms
- [SimpleIIR](./simpleiir.md)
  The simple IIR filter algorithm.
- [TwelvePtMovingWindowAverage](./twelveptmovingwindowaverage.md)
  The 12-point moving window average filter algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioclockalgorithm/raw)*