# vDSP_biquadm_ResetStateD

**Framework**: Accelerate  
**Kind**: func

Resets the filter state of a double-precision multichannel biquadratic IIR filter object.

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
extern void vDSP_biquadm_ResetStateD(vDSP_biquadm_SetupD __setup);
```

#### Discussion

This function is the same as [`vDSP_biquadm_ResetState`](https://developer.apple.com/documentation/kernel/1579974-vdsp_biquadm_resetstate) except for the type of the `setup` object.

## See Also

- [vDSP_biquadm_ResetState](vdsp_biquadm_resetstate.md)
  Resets the filter state of a single-precision multichannel biquadratic IIR filter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_resetstated)*