# Fast Fourier transforms

**Framework**: Accelerate

Transform vectors and matrices of temporal and spatial domain complex values to the frequency domain, and vice versa.

#### Overview

> 💡 **Tip**:  Where possible, use discrete Fourier transforms  (DFTs) instead of fast Fourier transforms (FFTs). DFTs provide a convenient API that offers greater flexibility over the number of elements the routines transform. vDSP’s DFT routines switch to FFT wherever possible.

For more information about DFTs, see [`Discrete Fourier transforms`](discrete-fourier-transforms.md).

## Topics

### Essentials
- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
  Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [Finding the component frequencies in a composite sine wave](finding-the-component-frequencies-in-a-composite-sine-wave.md)
  Use 1D fast Fourier transform to compute the frequency components of a signal.
- [Halftone descreening with 2D fast Fourier transform](halftone-descreening-with-2d-fast-fourier-transform.md)
  Reduce or remove periodic artifacts from images.
### Objects that Simplify FFTs
- [class FFT](vdsp/fft.md)
  A 1D single- and double-precision fast Fourier transform.
- [class FFT2D](vdsp/fft2d.md)
  A 2D single- and double-precision fast Fourier transform.
- [vDSP.FourierTransformDirection](vdsp/fouriertransformdirection.md)
  Fast Fourier transform directions.
- [vDSP.Radix](vdsp/radix.md)
  Fast Fourier transform radices.
### FFT Setup
- [vDSP_create_fftsetup](vdsp_create_fftsetup.md)
  Returns a setup structure that contains precalculated data for single-precision FFT functions.
- [vDSP_create_fftsetupD](vdsp_create_fftsetupd.md)
  Returns a setup structure that contains precalculated data for double-precision FFT functions.
- [vDSP_destroy_fftsetup](vdsp_destroy_fftsetup.md)
  Deallocates an existing single-precision FFT setup structure.
- [vDSP_destroy_fftsetupD](vdsp_destroy_fftsetupd.md)
  Deallocates an existing double-precision FFT setup structure.
- [vDSP_DFT_CreateSetup](vdsp_dft_createsetup.md)
- [typealias FFTSetup](fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTSetupD](fftsetupd.md)
  An opaque type that contains setup information for a double-precision FFT transform.
- [typealias FFTRadix](fftradix.md)
  The radix of the FFT decomposition.
### Functions for 1D Real FFT
- [In-Place Functions for 1D Real FFT](in-place-functions-for-1d-real-fft.md)
  Perform fast Fourier transforms in place on 1D real data.
- [Out-of-Place Functions for 1D Real FFT](out-of-place-functions-for-1d-real-fft.md)
  Perform fast Fourier transforms out of place on 1D real data.
- [vDSP_DFT_zop](vdsp_dft_zop.md)
### Functions for 1D Multiple-Signal Real FFT
- [In-Place Functions for 1D Multiple-Signal Real FFT](in-place-functions-for-1d-multiple-signal-real-fft.md)
  Perform fast Fourier transforms in place on multiple-signal 1D real data.
- [Out-of-Place Functions for 1D Multiple-Signal Real FFT](out-of-place-functions-for-1d-multiple-signal-real-fft.md)
  Perform fast Fourier transforms out of place on multiple-signal 1D real data.
### Functions for 1D Complex FFT
- [In-Place Functions for 1D Complex FFT](in-place-functions-for-1d-complex-fft.md)
  Perform fast Fourier transforms in place on 1D complex data.
- [Out-of-Place Functions for 1D Complex FFT](out-of-place-functions-for-1d-complex-fft.md)
  Perform fast Fourier transforms out of place on 1D complex data.
### Functions for 1D Multiple-Signal Complex FFT
- [In-Place Functions for 1D Multiple-Signal Complex FFT](in-place-functions-for-1d-multiple-signal-complex-fft.md)
  Perform fast Fourier transforms in place on multiple-signal 1D complex data.
- [Out-of-Place Functions for 1D Multiple-Signal Complex FFT](out-of-place-functions-for-1d-multiple-signal-complex-fft.md)
  Perform fast Fourier transforms out of place on multiple-signal 1D complex data.
### Functions for 2D Real FFT
- [In-Place Functions for 2D Real FFT](in-place-functions-for-2d-real-fft.md)
  Perform fast Fourier transforms in place on 2D real data.
- [Out-of-Place Functions for 2D Real FFT](out-of-place-functions-for-2d-real-fft.md)
  Perform fast Fourier transforms out of place on 2D real data.
### Functions for 2D Complex FFT
- [In-Place Functions for 2D Complex FFT](in-place-functions-for-2d-complex-fft.md)
  Perform fast Fourier transforms in place on 2D complex data.
- [Out-of-Place Functions for 2D Complex FFT](out-of-place-functions-for-2d-complex-fft.md)
  Perform fast Fourier transforms out of place on 2D complex data.
### Constants
- [typealias FFTDirection](fftdirection.md)
  Constants that specify whether to perform a forward or inverse FFT.
- [var FFT_FORWARD: Int](fft_forward.md)
  Forward FFT.
- [var FFT_INVERSE: Int](fft_inverse.md)
  Inverse FFT.
- [var FFT_RADIX2: Int](fft_radix2.md)
- [var FFT_RADIX3: Int](fft_radix3.md)
- [var FFT_RADIX5: Int](fft_radix5.md)
- [var kFFTDirection_Forward: Int](kfftdirection_forward.md)
- [var kFFTDirection_Inverse: Int](kfftdirection_inverse.md)
- [var kFFTRadix2: Int](kfftradix2.md)
- [var kFFTRadix3: Int](kfftradix3.md)
- [var kFFTRadix5: Int](kfftradix5.md)

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
- [Discrete Fourier transforms](discrete-fourier-transforms.md)
  Transform vectors of temporal and spatial domain complex values to the frequency domain, and vice versa.
- [Discrete Cosine transforms](discrete-cosine-transforms.md)
  Transform vectors of temporal and spatial domain real values to the frequency domain, and vice versa.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fast-fourier-transforms)*