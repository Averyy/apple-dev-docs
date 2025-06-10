# vDSP_biquad_DestroySetupD

**Framework**: Accelerate  
**Kind**: func

Destroys a double-precision biquadratic filter setup object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_biquad_DestroySetupD(vDSP_biquad_SetupD __setup);
```

#### Discussion

This function is the same as [`vDSP_biquadm_DestroySetup`](https://developer.apple.com/documentation/kernel/1579970-vdsp_biquadm_destroysetup), except for the type of the `setup` parameter.

## Parameters

- `__setup`: The object to be destroyed; a setup created by  .

## See Also

- [vDSP_biquad_DestroySetup](vdsp_biquad_destroysetup.md)
  Destroys a single-precision biquadratic filter setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquad_destroysetupd)*