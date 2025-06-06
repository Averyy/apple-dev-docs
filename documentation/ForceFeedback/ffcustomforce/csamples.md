# cSamples

**Framework**: Force Feedback  
**Kind**: property

Total number of samples in the . It must be an integral multiple of the .

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var cSamples: DWORD
```

## See Also

- [var cChannels: DWORD](ffcustomforce/cchannels.md)
  Number of channels (axes) affected by this force.
- [var dwSamplePeriod: DWORD](ffcustomforce/dwsampleperiod.md)
  Sample period, in microseconds.
- [var rglForceData: LPLONG!](ffcustomforce/rglforcedata.md)
  Pointer to an array of force values representing the custom force. If multiple channels are provided, the values are interleaved. For example, if  is 3, the first element of the array belongs to the first channel, the second to the second, and the third to the third.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcustomforce/csamples)*