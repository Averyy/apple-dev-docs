# vDSP_biquadm_CopyStateD

**Framework**: Accelerate  
**Kind**: func

Copies the filter state from one double-precision multichannel biquadratic IIR filter object to another.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_biquadm_CopyStateD(vDSP_biquadm_SetupD __dest, const struct vDSP_biquadm_SetupStructD * __src);
```

#### Discussion

This function is the same as [`vDSP_biquadm_CopyState`](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate), except for the types of the `src` and `dest` objects.

## See Also

- [vDSP_biquadm_CopyState](vdsp_biquadm_copystate.md)
  Copies the filter state from one single-precision multichannel biquadratic IIR filter object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_copystated)*