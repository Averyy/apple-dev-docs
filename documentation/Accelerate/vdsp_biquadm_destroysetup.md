# vDSP_biquadm_DestroySetup

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Destroys a single-precision multichannel biquadratic filter setup object.

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
extern void vDSP_biquadm_DestroySetup(vDSP_biquadm_Setup __setup);
```

#### Discussion

This function frees all resources associated with a biquadratic filter setup object.

## Parameters

- `__setup`: The biquadratic filter setup object that the function destroys.

## See Also

### Destroying a multichannel biquadratic filter setup
- [vDSP_biquadm_DestroySetupD](./vdsp_biquadm_destroysetupd.md)
  Destroys a double-precision multichannel biquadratic filter setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_destroysetup)*