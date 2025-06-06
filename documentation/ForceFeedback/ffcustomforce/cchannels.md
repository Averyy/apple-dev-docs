# cChannels

**Framework**: Force Feedback  
**Kind**: property

Number of channels (axes) affected by this force.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var cChannels: DWORD
```

#### Discussion

The first channel is applied to the first axis associated with the effect, the second to the second, and so on. If there are fewer channels than axes, nothing is associated with the extra axes.

If there is only a single channel, the effect is rotated in the direction specified by the rglDirection member of the FFEFFECT structure. If there is more than one channel, rotation is not allowed.

Not all devices support rotation of custom effects.

## See Also

- [var cSamples: DWORD](ffcustomforce/csamples.md)
  Total number of samples in the . It must be an integral multiple of the .
- [var dwSamplePeriod: DWORD](ffcustomforce/dwsampleperiod.md)
  Sample period, in microseconds.
- [var rglForceData: LPLONG!](ffcustomforce/rglforcedata.md)
  Pointer to an array of force values representing the custom force. If multiple channels are provided, the values are interleaved. For example, if  is 3, the first element of the array belongs to the first channel, the second to the second, and the third to the third.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcustomforce/cchannels)*