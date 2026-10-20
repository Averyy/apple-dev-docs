# dwSamplePeriod

**Framework**: Force Feedback  
**Kind**: property  
**Role**: Instance Property

Sample period, in microseconds.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var dwSamplePeriod: DWORD
```

```c
DWORD dwSamplePeriod;
```

## See Also

### Instance Properties
- [var cChannels: DWORD](./cchannels.md)
  Number of channels (axes) affected by this force.
- [var cSamples: DWORD](./csamples.md)
  Total number of samples in the **rglForceData**. It must be an integral multiple of the **cChannels**.
- [var rglForceData: LPLONG!](./rglforcedata.md)
  Pointer to an array of force values representing the custom force. If multiple channels are provided, the values are interleaved. For example, if **cChannels** is 3, the first element of the array belongs to the first channel, the second to the second, and the third to the third.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcustomforce/dwsampleperiod)*