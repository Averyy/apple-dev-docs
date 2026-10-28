# vDSP_biquadm_CopyState

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Copies the filter state from one single-precision multichannel biquadratic IIR filter object to another.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_biquadm_CopyState(vDSP_biquadm_Setup __dest, const struct vDSP_biquadm_SetupStruct *__src);
```

## Discussion

Both `src` and `dest` objects must be valid single-precision multichannel biquad setup objects created by previous calls to [`vDSP_biquadm_CreateSetup`](../kernel/api-1579945-vdsp_biquadm_createsetup.md), and both objects must have the same number of channels and sections.

## Parameters

- `__dest`: The `vDSP_biquadm_Setup` object whose state you wish to overwrite.
- `__src`: The `vDSP_biquadm_SetupStruct` object whose state you wish to copy.

## See Also

### Copying the filter state of a multichannel biquadratic filter
- [vDSP_biquadm_CopyStateD](./vdsp_biquadm_copystated.md)
  Copies the filter state from one double-precision multichannel biquadratic IIR filter object to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_copystate)*