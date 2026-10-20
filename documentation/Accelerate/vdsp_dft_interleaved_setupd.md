# vDSP_DFT_Interleaved_SetupD

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

An opaque type that contains setup information for an interleaved double-precision discrete Fourier transform (DFT).

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
typealias vDSP_DFT_Interleaved_SetupD = OpaquePointer
```

```c
typedef struct vDSP_DFT_Interleaved_SetupStructD * vDSP_DFT_Interleaved_SetupD;
```

#### Discussion

Call the [`vDSP_DFT_Interleaved_CreateSetupD(_:_:_:_:)`](./vdsp_dft_interleaved_createsetupd%28_,_,_,_%29.md) function to initialize and allocate a new setup object. Call [`vDSP_DFT_Interleaved_DestroySetupD(_:)`](./vdsp_dft_interleaved_destroysetupd%28_%29.md) to free the resources associated with a setup object.

## See Also

### Data types
- [typealias vDSP_DFT_Interleaved_Setup](./vdsp_dft_interleaved_setup.md)
  An opaque type that contains setup information for an interleaved single-precision discrete Fourier transform (DFT).
- [typealias vDSP_DFT_Setup](./vdsp_dft_setup.md)
  An opaque type that contains setup information for a single-precision discrete Fourier transform (DFT).
- [typealias vDSP_DFT_SetupD](./vdsp_dft_setupd.md)
  An opaque type that contains setup information for a double-precision discrete Fourier transform (DFT).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_interleaved_setupd)*