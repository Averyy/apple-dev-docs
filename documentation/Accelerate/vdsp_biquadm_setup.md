# vDSP_biquadm_Setup

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

A data structure that contains precalculated data for use by a single-precision, multichannel cascaded biquadratic filter function.

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
typealias vDSP_biquadm_Setup = OpaquePointer
```

```c
typedef struct vDSP_biquadm_SetupStruct * vDSP_biquadm_Setup;
```

## See Also

### Creating a multichannel biquadratic filter setup
- [typealias vDSP_biquadm_SetupD](./vdsp_biquadm_setupd.md)
  A data structure that contains precalculated data for use by a double-precision, multichannel cascaded biquadratic filter function.
- [vDSP_biquadm_CreateSetup](./vdsp_biquadm_createsetup.md)
  Builds a data structure that contains precalculated data for use by a single-precision, multichannel cascaded biquadratic filter function.
- [vDSP_biquadm_CreateSetupD](./vdsp_biquadm_createsetupd.md)
  Builds a data structure that contains precalculated data for use by a double-precision, multichannel cascaded biquadratic filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_setup)*