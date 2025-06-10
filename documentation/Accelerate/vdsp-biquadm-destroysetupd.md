# vDSP_biquadm_DestroySetupD

**Framework**: Accelerate  
**Kind**: func

Destroys a double-precision multichannel biquadratic filter setup object.

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
extern void vDSP_biquadm_DestroySetupD(vDSP_biquadm_SetupD __setup);
```

#### Discussion

This function frees all resources associated with a biquadratic filter setup object.

## Parameters

- `__setup`: The biquadratic filter setup object that the function destroys.

## See Also

- [vDSP_biquadm_DestroySetup](vdsp_biquadm_destroysetup.md)
  Destroys a single-precision multichannel biquadratic filter setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_destroysetupd)*