# vDSP_DFT_Interleaved_DestroySetup(_:)

**Framework**: Accelerate  
**Kind**: func

Releases a single-precision discrete Fourier transform (DFT) setup structure.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func vDSP_DFT_Interleaved_DestroySetup(_ Setup: vDSP_DFT_Interleaved_Setup?)
```

#### Discussion

> ❗ **Important**:  This function isn’t fully thread-safe. Don’t call this function concurrently with any function that uses or shares its underlying storage with the setup structure.

## Parameters

- `Setup`: The setup structure to destroy.

## See Also

- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
  Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [func vDSP_DFT_Interleaved_CreateSetup(vDSP_DFT_Interleaved_Setup?, vDSP_Length, vDSP_DFT_Direction, vDSP_DFT_RealtoComplex) -> vDSP_DFT_Interleaved_Setup?](vdsp_dft_interleaved_createsetup(_:_:_:_:).md)
  Returns a setup structure that contains precalculated data for forward and inverse, single-precision interleaved discrete Fourier transform (DFT) functions.
- [func vDSP_DFT_Interleaved_CreateSetupD(vDSP_DFT_Interleaved_SetupD?, vDSP_Length, vDSP_DFT_Direction, vDSP_DFT_RealtoComplex) -> vDSP_DFT_Interleaved_SetupD?](vdsp_dft_interleaved_createsetupd(_:_:_:_:).md)
  Returns a setup structure that contains precalculated data for forward and inverse, double-precision interleaved discrete Fourier transform (DFT) functions.
- [func vDSP_DFT_Interleaved_Execute(vDSP_DFT_Interleaved_Setup, UnsafePointer<DSPComplex>, UnsafeMutablePointer<DSPComplex>)](vdsp_dft_interleaved_execute(_:_:_:).md)
  Calculates the single-precision discrete Fourier transform (DFT)  for a vector of interleaved complex values.
- [func vDSP_DFT_Interleaved_ExecuteD(vDSP_DFT_Interleaved_SetupD, UnsafePointer<DSPDoubleComplex>, UnsafeMutablePointer<DSPDoubleComplex>)](vdsp_dft_interleaved_executed(_:_:_:).md)
  Calculates the double-precision discrete Fourier transform (DFT) for a vector of interleaved complex values.
- [func vDSP_DFT_Interleaved_DestroySetupD(vDSP_DFT_Interleaved_SetupD?)](vdsp_dft_interleaved_destroysetupd(_:).md)
  Releases a double-precision discrete Fourier transform (DFT) setup structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_interleaved_destroysetup(_:))*