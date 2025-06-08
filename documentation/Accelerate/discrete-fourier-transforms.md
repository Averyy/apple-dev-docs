# Discrete Fourier transforms

**Framework**: Accelerate

Transform vectors of temporal and spatial domain complex values to the frequency domain, and vice versa.

## Topics

### Objects that simplify discrete Fourier transforms
- [class DiscreteFourierTransform](vdsp/discretefouriertransform.md)
  An object that provides forward and inverse discrete Fourier transforms on single- or double-precision collections of interleaved or split-complex data.
- [vDSP.DFTTransformType](vdsp/dfttransformtype.md)
  Discrete Fourier transform types.
- [class DFT](vdsp/dft.md)
  A single- and double-precision discrete Fourier transform.
### Interleaved discrete Fourier transform functions
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
- [func vDSP_DFT_Interleaved_DestroySetup(vDSP_DFT_Interleaved_Setup?)](vdsp_dft_interleaved_destroysetup(_:).md)
  Releases a single-precision discrete Fourier transform (DFT) setup structure.
- [func vDSP_DFT_Interleaved_DestroySetupD(vDSP_DFT_Interleaved_SetupD?)](vdsp_dft_interleaved_destroysetupd(_:).md)
  Releases a double-precision discrete Fourier transform (DFT) setup structure.
### Real discrete Fourier transform setup
- [vDSP_DFT_zrop_CreateSetup](vdsp_dft_zrop_createsetup.md)
  Returns a setup structure that contains precalculated data for forward and inverse, real, single-precision DFT functions.
- [vDSP_DFT_zrop_CreateSetupD](vdsp_dft_zrop_createsetupd.md)
  Returns a setup structure that contains precalculated data for forward and inverse, real, double-precision DFT functions.
### Complex discrete Fourier transform setup
- [vDSP_DFT_zop_CreateSetup](vdsp_dft_zop_createsetup.md)
  Returns a setup structure that contains precalculated data for forward and inverse, complex, single-precision DFT functions.
- [vDSP_DFT_zop_CreateSetupD](vdsp_dft_zop_createsetupd.md)
  Returns a setup structure that contains precalculated data for forward and inverse, complex, double-precision DFT functions.
### Functions to perform discrete Fourier transforms
- [vDSP_DFT_Execute](vdsp_dft_execute.md)
  Calculates the discrete single-precision Fourier transform for a vector.
- [vDSP_DFT_ExecuteD](vdsp_dft_executed.md)
  Calculates the discrete double-precision Fourier transform for a vector.
### Discrete Fourier transform cleanup
- [vDSP_DFT_DestroySetup](vdsp_dft_destroysetup.md)
  Releases a single-precision setup structure.
- [vDSP_DFT_DestroySetupD](vdsp_dft_destroysetupd.md)
  Releases a double-precision setup structure.
### Data types
- [typealias vDSP_DFT_Interleaved_Setup](vdsp_dft_interleaved_setup.md)
  An opaque type that contains setup information for an interleaved single-precision discrete Fourier transform (DFT).
- [typealias vDSP_DFT_Interleaved_SetupD](vdsp_dft_interleaved_setupd.md)
  An opaque type that contains setup information for an interleaved double-precision discrete Fourier transform (DFT).
- [typealias vDSP_DFT_Setup](vdsp_dft_setup.md)
  An opaque type that contains setup information for a single-precision discrete Fourier transform (DFT).
- [typealias vDSP_DFT_SetupD](vdsp_dft_setupd.md)
  An opaque type that contains setup information for a double-precision discrete Fourier transform (DFT).
### Constants
- [enum vDSP_DFT_Direction](vdsp_dft_direction.md)
  An enumeration that specifies whether to perform a forward or inverse DFT.
### Enumerations
- [enum vDSP_DFT_RealtoComplex](vdsp_dft_realtocomplex.md)

## See Also

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Finding the component frequencies in a composite sine wave](finding-the-component-frequencies-in-a-composite-sine-wave.md)
  Use 1D fast Fourier transform to compute the frequency components of a signal.
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
  Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [Signal extraction from noise](signal-extraction-from-noise.md)
  Use Accelerate’s discrete cosine transform to remove noise from a signal.
- [Performing Fourier Transforms on Multiple Signals](performing-fourier-transforms-on-multiple-signals.md)
  Use Accelerate’s multiple-signal fast Fourier transform (FFT) functions to transform multiple signals with a single function call.
- [Halftone descreening with 2D fast Fourier transform](halftone-descreening-with-2d-fast-fourier-transform.md)
  Reduce or remove periodic artifacts from images.
- [Fast Fourier transforms](fast-fourier-transforms.md)
  Transform vectors and matrices of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Cosine transforms](discrete-cosine-transforms.md)
  Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/discrete-fourier-transforms)*