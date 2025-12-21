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
- [typealias vDSP_biquadm_Setup](vdsp_biquadm_setup.md)
  A data structure that contains precalculated data for use by a single-precision, multichannel cascaded biquadratic filter function.
- [typealias vDSP_biquadm_SetupD](vdsp_biquadm_setupd.md)
  A data structure that contains precalculated data for use by a double-precision, multichannel cascaded biquadratic filter function.

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