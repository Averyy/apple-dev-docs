# rglForceData

**Framework**: Force Feedback  
**Kind**: property

Pointer to an array of force values representing the custom force. If multiple channels are provided, the values are interleaved. For example, if  is 3, the first element of the array belongs to the first channel, the second to the second, and the third to the third.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var rglForceData: LPLONG!
```

## See Also

- [var cChannels: DWORD](ffcustomforce/cchannels.md)
  Number of channels (axes) affected by this force.
- [var cSamples: DWORD](ffcustomforce/csamples.md)
  Total number of samples in the . It must be an integral multiple of the .
- [var dwSamplePeriod: DWORD](ffcustomforce/dwsampleperiod.md)
  Sample period, in microseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcustomforce/rglforcedata)*