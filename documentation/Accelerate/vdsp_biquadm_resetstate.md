# vDSP_biquadm_ResetState

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Resets the filter state of a single-precision multichannel biquadratic IIR filter object.

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
extern void vDSP_biquadm_ResetState(vDSP_biquadm_Setup __setup);
```

## Discussion

The `setup` object must be a valid object, previously initialized by a call to the [`vDSP_biquadm_CreateSetup`](../kernel/api-1579945-vdsp_biquadm_createsetup.md) function. Upon return, all internal state is reset to the values it had when it was first initialized.

## Parameters

- `__setup`: The filter state object whose state you wish to reset.

## See Also

### Resetting the filter state of a multichannel biquadratic filter
- [vDSP_biquadm_ResetStateD](./vdsp_biquadm_resetstated.md)
  Resets the filter state of a double-precision multichannel biquadratic IIR filter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_resetstate)*