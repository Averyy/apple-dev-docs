# Multichannel biquadratic filters

**Framework**: Accelerate

Filter a multichannel signal with a cascade of biquadratic sections.

#### Overview

The vDSP library implements biquadratic filtering as a cascade of individual infinite impulse response (IIR) filters called  Each section has its own set of feedback and feedforward coefficients, and implements a direct-form 2 filter.

When the biquadratic filter function executes, the sections execute in sequence. Each section processes the entire input signal and passes its output to the next section for further processing.

> **Note**:  The vDSP biquadratic filters work in place. That is, the source and destination pointers may point to the same memory.

> **Note**:  Although you can use [`vDSP_biquadm`](https://developer.apple.com/documentation/kernel/1579994-vdsp_biquadm) to process a single channel of data, it’s optimized for processing multiple channels of data independently. When processing only a single channel, the single-channel API [`vDSP_biquad`](vdsp_biquad.md) may provide better performance and energy efficiency. When processing a single channel in isolation, it’s best practice to use [`vDSP_biquad`](vdsp_biquad.md) whenever possible.

## Topics

### Equalizing audio with biquadratic filters
- [Equalizing audio with discrete cosine transforms (DCTs)](equalizing-audio-with-discrete-cosine-transforms-dcts.md)
  Change the frequency response of an audio signal by manipulating frequency-domain data.
### Creating a multichannel biquadratic filter setup
- [vDSP_biquadm_CreateSetup](vdsp_biquadm_createsetup.md)
  Builds a data structure that contains precalculated data for use by a single-precision, multichannel cascaded biquadratic filter function.
- [typealias vDSP_biquadm_Setup](vdsp_biquadm_setup.md)
  A data structure that contains precalculated data for use by a single-precision, multichannel cascaded biquadratic filter function.
- [vDSP_biquadm_CreateSetupD](vdsp_biquadm_createsetupd.md)
  Builds a data structure that contains precalculated data for use by a double-precision, multichannel cascaded biquadratic filter function.
- [typealias vDSP_biquadm_SetupD](vdsp_biquadm_setupd.md)
  A data structure that contains precalculated data for use by a double-precision, multichannel cascaded biquadratic filter function.
### Copying the filter state of a multichannel biquadratic filter
- [vDSP_biquadm_CopyState](vdsp_biquadm_copystate.md)
  Copies the filter state from one single-precision multichannel biquadratic IIR filter object to another.
- [vDSP_biquadm_CopyStateD](vdsp_biquadm_copystated.md)
  Copies the filter state from one double-precision multichannel biquadratic IIR filter object to another.
### Resetting the filter state of a multichannel biquadratic filter
- [vDSP_biquadm_ResetState](vdsp_biquadm_resetstate.md)
  Resets the filter state of a single-precision multichannel biquadratic IIR filter object.
- [vDSP_biquadm_ResetStateD](vdsp_biquadm_resetstated.md)
  Resets the filter state of a double-precision multichannel biquadratic IIR filter object.
### Setting the filter state of a multichannel biquadratic filter
- [vDSP_biquadm_SetActiveFilters](vdsp_biquadm_setactivefilters.md)
  Activates or deactivates individual sections in a single-precision, multichannel biquadratic filter.
- [vDSP_biquadm_SetActiveFiltersD](vdsp_biquadm_setactivefiltersd.md)
  Activates or deactivates individual sections in a double-precision, multichannel biquadratic filter.
### Setting the coefficients of a multichannel biquadratic filter
- [vDSP_biquadm_SetCoefficientsSingle](vdsp_biquadm_setcoefficientssingle.md)
  Sets the single-precision coefficients of the specified single-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetCoefficientsDouble](vdsp_biquadm_setcoefficientsdouble.md)
  Sets the double-precision coefficients of the specified single-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetCoefficientsSingleD](vdsp_biquadm_setcoefficientssingled.md)
  Sets the single-precision coefficients of the specified double-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetCoefficientsDoubleD](vdsp_biquadm_setcoefficientsdoubled.md)
  Sets the double-precision coefficients of the specified double-precision, multichannel biquadratic filter setup object.
### Setting the target values of a multichannel biquadratic filter
- [vDSP_biquadm_SetTargetsSingle](vdsp_biquadm_settargetssingle.md)
  Sets the single-precision coefficient target values of the specified single-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetTargetsDouble](vdsp_biquadm_settargetsdouble.md)
  Sets the double-precision coefficient target values of the specified single-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetTargetsSingleD](vdsp_biquadm_settargetssingled.md)
  Sets the single-precision coefficient target values of the specified double-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetTargetsDoubleD](vdsp_biquadm_settargetsdoubled.md)
  Sets the double-precision coefficient target values of the specified double-precision, multichannel biquadratic filter setup object.
### Applying a multichannel biquadratic filter
- [vDSP_biquadm](vdsp_biquadm.md)
  Applies a single-precision multichannel biquadratic IIR filter.
- [vDSP_biquadmD](vdsp_biquadmd.md)
  Applies a double-precision multichannel biquadratic IIR filter.
### Destroying a multichannel biquadratic filter setup
- [vDSP_biquadm_DestroySetup](vdsp_biquadm_destroysetup.md)
  Destroys a single-precision multichannel biquadratic filter setup object.
- [vDSP_biquadm_DestroySetupD](vdsp_biquadm_destroysetupd.md)
  Destroys a double-precision multichannel biquadratic filter setup object.

## See Also

- [Biquadratic IIR filters](biquadratic-iir-filters.md)
  Apply biquadratic filters to single-channel and multichannel data.
- [Single-channel biquadratic filters](single-channel-biquadratic-filters.md)
  Filter a single-channel signal with a cascade of biquadratic sections.
- [Finite impulse response filters](finite-impulse-response-filters.md)
  Perform finite impulse response filtering with decimation and antialiasing on vectors of real or complex values.
- [Recursive filters](recursive-filters.md)
  Perform two-pole two-zero recursive filtering on a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/multichannel-biquadratic-filters)*