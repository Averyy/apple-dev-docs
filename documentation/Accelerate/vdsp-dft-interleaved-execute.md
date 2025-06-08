# vDSP_DFT_Interleaved_Execute(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision discrete Fourier transform (DFT)  for a vector of interleaved complex values.

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
func vDSP_DFT_Interleaved_Execute(_ Setup: vDSP_DFT_Interleaved_Setup, _ Iri: UnsafePointer<DSPComplex>, _ Ori: UnsafeMutablePointer<DSPComplex>)
```

#### Discussion

This function supports in-place operation where the output and input parameters are equal. The transform length must equal the transform length specified in the setup structure.

> ❗ **Important**:  For best performance, make sure the two vector addresses you pass to this function are 16-byte-aligned.

## Parameters

- `Setup`: The DFT setup structure for this transform.
- `Iri`: A single-precision vector that contains the input values.
- `Ori`: A single-precision vector that contains the output values. The output can equal the input, but this function doesn’t support any other overlap of the input and output vectors.

## See Also

- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
  Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [func vDSP_DFT_Interleaved_CreateSetup(vDSP_DFT_Interleaved_Setup?, vDSP_Length, vDSP_DFT_Direction, vDSP_DFT_RealtoComplex) -> vDSP_DFT_Interleaved_Setup?](vdsp_dft_interleaved_createsetup(_:_:_:_:).md)
  Returns a setup structure that contains precalculated data for forward and inverse, single-precision interleaved discrete Fourier transform (DFT) functions.
- [func vDSP_DFT_Interleaved_CreateSetupD(vDSP_DFT_Interleaved_SetupD?, vDSP_Length, vDSP_DFT_Direction, vDSP_DFT_RealtoComplex) -> vDSP_DFT_Interleaved_SetupD?](vdsp_dft_interleaved_createsetupd(_:_:_:_:).md)
  Returns a setup structure that contains precalculated data for forward and inverse, double-precision interleaved discrete Fourier transform (DFT) functions.
- [func vDSP_DFT_Interleaved_ExecuteD(vDSP_DFT_Interleaved_SetupD, UnsafePointer<DSPDoubleComplex>, UnsafeMutablePointer<DSPDoubleComplex>)](vdsp_dft_interleaved_executed(_:_:_:).md)
  Calculates the double-precision discrete Fourier transform (DFT) for a vector of interleaved complex values.
- [func vDSP_DFT_Interleaved_DestroySetup(vDSP_DFT_Interleaved_Setup?)](vdsp_dft_interleaved_destroysetup(_:).md)
  Releases a single-precision discrete Fourier transform (DFT) setup structure.
- [func vDSP_DFT_Interleaved_DestroySetupD(vDSP_DFT_Interleaved_SetupD?)](vdsp_dft_interleaved_destroysetupd(_:).md)
  Releases a double-precision discrete Fourier transform (DFT) setup structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_interleaved_execute(_:_:_:))*