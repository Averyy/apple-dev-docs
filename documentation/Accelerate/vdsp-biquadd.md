# vDSP_biquadD

**Framework**: Accelerate  
**Kind**: func

Applies a double-precision single-channel biquadratic IIR filter.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_biquadD(const struct vDSP_biquad_SetupStructD * __Setup, double * __Delay, const double * __X, vDSP_Stride __IX, double * __Y, vDSP_Stride __IY, vDSP_Length __N);
```

#### Discussion

This function is the same as [`vDSP_biquad`](vdsp_biquad.md), except for the types of arrays `Delay`, `X`, and `Y`.

## Parameters

- `__Setup`: The   object defining the filter to apply.
- `__Delay`: An array of double-precision values initialized with “past” state data (elements -2 and -1) for each section of the biquad. After this function executes, this array contains the final state data of the filters. See Discussion below.
- `__X`: An array of double-precision input data for the channel.
- `__IX`: Stride for  .
- `__Y`: An array to be filled with double-precision output data for the channel.
- `__IY`: Stride for  .
- `__N`: The number of elements to filter.

## See Also

- [vDSP_biquad](vdsp_biquad.md)
  Applies a single-precision single-channel biquadratic IIR filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadd)*