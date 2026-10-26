# vDSP_biquad_Setup

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

A data structure that contains precalculated data for use by the single-precision cascaded biquadratic IIR filter function.

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
typealias vDSP_biquad_Setup = OpaquePointer
```

```c
typedef struct vDSP_biquad_SetupStruct * vDSP_biquad_Setup;
```

## See Also

### Creating a single-channel biquadratic filter setup
- [typealias vDSP_biquad_SetupD](./vdsp_biquad_setupd.md)
  A data structure that contains precalculated data for use by the double-precision cascaded biquadratic IIR filter function.
- [vDSP_biquad_CreateSetup](./vdsp_biquad_createsetup.md)
  Builds a data structure that contains precalculated data for use by a single-precision cascaded biquadratic filter function.
- [vDSP_biquad_CreateSetupD](./vdsp_biquad_createsetupd.md)
  Builds a data structure that contains precalculated data for use by a double-precision cascaded biquadratic filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquad_setup)*