# vDSP_biquad_SetupD

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

A data structure that contains precalculated data for use by the double-precision cascaded biquadratic IIR filter function.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias vDSP_biquad_SetupD = OpaquePointer
```

```c
typedef struct vDSP_biquad_SetupStructD * vDSP_biquad_SetupD;
```

## See Also

### Creating a single-channel biquadratic filter setup
- [typealias vDSP_biquad_Setup](./vdsp_biquad_setup.md)
  A data structure that contains precalculated data for use by the single-precision cascaded biquadratic IIR filter function.
- [vDSP_biquad_CreateSetup](./vdsp_biquad_createsetup.md)
  Builds a data structure that contains precalculated data for use by a single-precision cascaded biquadratic filter function.
- [vDSP_biquad_CreateSetupD](./vdsp_biquad_createsetupd.md)
  Builds a data structure that contains precalculated data for use by a double-precision cascaded biquadratic filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquad_setupd)*