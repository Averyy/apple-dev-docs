# Discrete Cosine transforms

**Framework**: Accelerate

Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.

## Topics

### First Steps
- [Signal extraction from noise](signal-extraction-from-noise.md)
  Use Accelerate’s discrete cosine transform to remove noise from a signal.
- [Equalizing audio with discrete cosine transforms (DCTs)](equalizing-audio-with-discrete-cosine-transforms-dcts.md)
  Change the frequency response of an audio signal by manipulating frequency-domain data.
### Objects that Simplify Discrete Cosine Transforms
- [class DCT](vdsp/dct.md)
  A single-precision discrete cosine transform.
- [vDSP.DCTTransformType](vdsp/dcttransformtype.md)
  An enumeration that describes the discrete cosine transform types.
### Discrete Cosine Transforms
- [vDSP_DCT_CreateSetup](vdsp_dct_createsetup.md)
  Builds a data structure that contains precalculated data to perform a discrete cosine transform.
- [enum vDSP_DCT_Type](vdsp_dct_type.md)
  Constants that indicate the type for a discrete cosine transform.
- [vDSP_DCT_Execute](vdsp_dct_execute.md)
  Calculates the discrete cosine transform for a vector.

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
- [Discrete Fourier transforms](discrete-fourier-transforms.md)
  Transform vectors of temporal and spatial domain complex values to the frequency domain, and vice versa.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/discrete-cosine-transforms)*