# vDSP_biquad

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a single-precision single-channel biquadratic IIR filter.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_biquad(const struct vDSP_biquad_SetupStruct *__Setup, float *__Delay, const float *__X, vDSP_Stride __IX, float *__Y, vDSP_Stride __IY, vDSP_Length __N);
```

## Discussion

This function applies a cascaded biquad filter to the input values in `X`, and places the results in `Y`.

The state contained in the `setup` object is updated upon return.

## Parameters

- `__Setup`: The [`vDSP_biquad_Setup`](../kernel/vdsp_biquad_setup.md) object defining the filter to apply.
- `__Delay`: An array of single-precision values initialized with direct-form 1 “past” state data for each section of the biquad. The length of the array should be (2 * `M`) + 2, where `M` is the number of sections. For each section *m*, `Delay`[2**m*:2**m*+1] represent the two delayed input values for section *m* and `Delay`[2*`M`:2*`M`+1] represent the two delayed output values of the filter.  After this function executes, this array contains the final state data of the filters.
- `__X`: An array of single-precision input data for the channel.
- `__IX`: Stride for `X`.
- `__Y`: An array to be filled with single-precision output data for the channel.
- `__IY`: Stride for`Y`.
- `__N`: The number of elements to filter.

## See Also

### Applying a single-channel biquadratic filter
- [vDSP_biquadD](./vdsp_biquadd.md)
  Applies a double-precision single-channel biquadratic IIR filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquad)*