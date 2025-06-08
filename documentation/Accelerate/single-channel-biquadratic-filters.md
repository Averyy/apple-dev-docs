# Single-channel biquadratic filters

**Framework**: Accelerate

Filter a single-channel signal with a cascade of biquadratic sections.

#### Overview

The vDSP library implements biquadratic filtering as a cascade of individual infinite impulse response (IIR) filters called  Each section has its own set of feedback and feedforward coefficients, and implements a direct-form 1 filter.

When the biquadratic filter function executes, the sections execute in sequence. Each section processes the entire input signal and passes its output to the next section for further processing.

> **Note**:  The vDSP biquadratic filters work in place. That is, the source and destination pointers may point to the same memory.

## Topics

### Biquadratic filter essentials
- [Applying biquadratic filters to a music loop](applying-biquadratic-filters-to-a-music-loop.md)
  Change the frequency response of an audio signal using a cascaded biquadratic filter.
- [Creating an audio unit extension using the vDSP library](creating-an-audio-unit-extension-using-the-vdsp-library.md)
  Add biquadratic filter audio-effect processing to apps like Logic Pro X and GarageBand with the Accelerate framework.
### Creating a single-channel biquadratic filter setup
- [vDSP_biquad_CreateSetup](vdsp_biquad_createsetup.md)
  Builds a data structure that contains precalculated data for use by a single-precision cascaded biquadratic filter function.
- [typealias vDSP_biquad_Setup](vdsp_biquad_setup.md)
  A data structure that contains precalculated data for use by the single-precision cascaded biquadratic IIR filter function.
- [vDSP_biquad_CreateSetupD](vdsp_biquad_createsetupd.md)
  Builds a data structure that contains precalculated data for use by a double-precision cascaded biquadratic filter function.
- [typealias vDSP_biquad_SetupD](vdsp_biquad_setupd.md)
  A data structure that contains precalculated data for use by the double-precision cascaded biquadratic IIR filter function.
### Applying a single-channel biquadratic filter
- [vDSP_biquad](vdsp_biquad.md)
  Applies a single-precision single-channel biquadratic IIR filter.
- [vDSP_biquadD](vdsp_biquadd.md)
  Applies a double-precision single-channel biquadratic IIR filter.
### Setting the coefficients of a single-channel biquadratic filter
- [vDSP_biquad_SetCoefficientsSingle](vdsp_biquad_setcoefficientssingle.md)
  Sets single-precision coefficients of the specified single-channel biquadratic filter setup object.
- [vDSP_biquad_SetCoefficientsDouble](vdsp_biquad_setcoefficientsdouble.md)
  Sets double-precision coefficients of the specified single-channel biquadratic filter setup object.
### Destroying a single-channel biquadratic filter setup
- [vDSP_biquad_DestroySetup](vdsp_biquad_destroysetup.md)
  Destroys a single-precision biquadratic filter setup object.
- [vDSP_biquad_DestroySetupD](vdsp_biquad_destroysetupd.md)
  Destroys a double-precision biquadratic filter setup object.

## See Also

- [Biquadratic IIR filters](biquadratic-iir-filters.md)
  Apply biquadratic filters to single-channel and multichannel data.
- [Multichannel biquadratic filters](multichannel-biquadratic-filters.md)
  Filter a multichannel signal with a cascade of biquadratic sections.
- [Finite impulse response filters](finite-impulse-response-filters.md)
  Perform finite impulse response filtering with decimation and antialiasing on vectors of real or complex values.
- [Recursive filters](recursive-filters.md)
  Perform two-pole two-zero recursive filtering on a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/single-channel-biquadratic-filters)*